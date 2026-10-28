<?php
// Send one message with plain cURL. Requires PHP 8+ with the curl extension.
$key = getenv('EBTEKAR_API_KEY');
if (!$key) {
    fwrite(STDERR, "Set EBTEKAR_API_KEY first\n");
    exit(1);
}

$payload = [
    'model' => 'ebtekar-smart',
    'max_tokens' => 1024,
    'messages' => [['role' => 'user', 'content' => 'سلام! یک جملهٔ خوش‌آمدگویی برای سایتم بنویس.']],
];

$ch = curl_init('https://ebtekarai.ir/api/developer-gateway/v1/messages');
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT => 60,
    CURLOPT_HTTPHEADER => [
        'x-api-key: ' . $key,
        'anthropic-version: 2023-06-01',
        'content-type: application/json',
    ],
    CURLOPT_POSTFIELDS => json_encode($payload, JSON_UNESCAPED_UNICODE),
]);

$body = curl_exec($ch);
$status = curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
curl_close($ch);

if ($status !== 200) {
    fwrite(STDERR, "HTTP $status: $body\n");
    exit(1);
}
$data = json_decode((string) $body, true);
echo $data['content'][0]['text'] ?? '', PHP_EOL;
