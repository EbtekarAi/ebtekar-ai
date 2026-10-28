# Examples · نمونه‌کدها

Runnable client samples for the Ebtekar Developer Gateway. Each one reads your key from the `EBTEKAR_API_KEY` environment variable — **never hard-code keys**.

نمونه‌کدهای آمادهٔ اجرا برای درگاه توسعه‌دهندگان ابتکار. همه کلید را از متغیر محیطی `EBTEKAR_API_KEY` می‌خوانند — **کلید را هرگز داخل کد ننویسید.**

| Folder | Run |
|---|---|
| `curl/` | `bash curl/messages.sh` · `bash curl/stream.sh` · `bash curl/models.sh` |
| `python/` | `pip install anthropic` → `python python/messages.py` · `stream.py` · `tools.py` |
| `node/` | `npm i @anthropic-ai/sdk` → `node node/messages.mjs` · `stream.mjs` · `tools.mjs` |
| `php/` | `php php/messages.php` (needs the cURL extension) |

```bash
# macOS / Linux
export EBTEKAR_API_KEY="ebt_live_..."
```

```powershell
# Windows PowerShell
$env:EBTEKAR_API_KEY="ebt_live_..."
```

Create a key at **https://ebtekarai.ir/developers**. Full guide: [English](../docs/developers.md) · [فارسی](../docs/developers.fa.md)
