import asyncio
import os
import sys

try:
    from pyppeteer import launch
except Exception as exc:
    print("pyppeteer not installed: ", exc)
    sys.exit(2)


async def html_to_pdf(input_path: str, output_path: str) -> None:
    browser = await launch(args=["--no-sandbox", "--disable-gpu"], headless=True)
    page = await browser.newPage()
    await page.goto(f"file://{os.path.abspath(input_path)}", {"waitUntil": "load"})
    await page.emulateMedia("screen")
    await page.pdf({
        "path": output_path,
        "format": "A4",
        "printBackground": True,
        "margin": {"top": "12mm", "bottom": "12mm", "left": "12mm", "right": "12mm"}
    })
    await browser.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: html_to_pdf.py <input.html> <output.pdf>")
        sys.exit(1)
    inp, outp = sys.argv[1], sys.argv[2]
    asyncio.get_event_loop().run_until_complete(html_to_pdf(inp, outp))