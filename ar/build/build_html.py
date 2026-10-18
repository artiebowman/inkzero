"""Build the proposal HTML from the Markdown master.

Run from the repo root or from ar/:
    python3 ar/build/build_html.py && python3 ar/build/build_pdf.py

Needs: pip install markdown
Reads  ar/InkZero_AR_Proposal_v3_2026-10-18.md and ar/figures/*.svg
Writes ar/build/InkZero_AR_Proposal.html (ignored by git)
"""
import base64
import re
from pathlib import Path

import markdown

HERE = Path(__file__).resolve().parent          # ar/build
AR = HERE.parent                                 # ar
MD = AR / "InkZero_AR_Proposal_v3_2026-10-18.md"
FIGURES = AR / "figures"
CSS = HERE / "proposal.css"
OUT = HERE / "InkZero_AR_Proposal.html"

src = MD.read_text(encoding="utf-8")
body = src.split("\n## Open items before Monday")[0]

figmap = {
    1: "fig1_row.svg",
    2: "fig2_placements.svg",
    3: None,  # Dreamborn screenshot, not made yet
    4: "fig4_pip_states.svg",
    5: "fig5_pipeline.svg",
    6: "fig6_mat.svg",
    7: "fig7_results_table.svg",
}


def repl(m):
    n = int(m.group(1))
    cap = m.group(2).strip()
    f = figmap.get(n)
    if f and (FIGURES / f).exists():
        data = base64.b64encode((FIGURES / f).read_bytes()).decode()
        img = f'<img src="data:image/svg+xml;base64,{data}" alt="Figure {n}">'
    else:
        img = (
            '<div class="placeholder">Figure 3 placeholder: Dreamborn screenshot '
            "of one of the chosen decks, to be added.</div>"
        )
    return f"<figure>{img}<figcaption><em>Figure {n}. {cap}</em></figcaption></figure>"


body = re.sub(r"^\[Figure (\d+): (.*?)\]$", repl, body, flags=re.M)

# page breaks before the longer sections
for h in [
    "**3. What each row shows.**",
    "**4. What I track to fill the rows.**",
    "**5. How it gets drawn.**",
    "## How I will test it",
]:
    body = body.replace("\n" + h, '\n<div class="pb"></div>\n\n' + h)

# keep the future-work list on one page
i = body.index("Future work, in the order it would come:")
j = body.index("\n## References")
body = body[:i] + '<div class="keep" markdown="1">\n\n' + body[i:j] + "\n\n</div>\n" + body[j:]

html = markdown.markdown(body, extensions=["tables", "md_in_html"]).replace("<hr />", "")
css = CSS.read_text(encoding="utf-8")
OUT.write_text(
    "<!doctype html><html><head><meta charset=\"utf-8\">"
    "<title>InkZero AR — Project Proposal</title>"
    f"<style>{css}</style></head><body>{html}</body></html>",
    encoding="utf-8",
)
print("html ok:", OUT)
