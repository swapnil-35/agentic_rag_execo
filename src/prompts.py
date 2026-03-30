EXTRACTION_PROMPT = """
Extract all fields in JSON:

{{
  "Document Type": "",
  "Effective Date": "",
  "Buyer": "",
  "Company (Target)": "",
  "Seller": "",
  "Shares Transacted": "",
  "Cash Purchase Price": "",
  "Escrow Agent": "",
  "Escrow Amount": "",
  "Target Working Capital": "",
  "Indemnification De Minimis Amount": "",
  "Indemnification Basket Amount": "",
  "Indemnification Cap Amount": "",
  "Governing Law": ""
}}

Return ONLY JSON.

Context:
{context}
"""


RETRY_PROMPT = """
Extract value for "{field}"

Return JSON:
{{"value": ""}}

Context:
{context}
"""