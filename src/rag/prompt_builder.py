"""
IndianMiningGPT
Phase 6.2 Prompt Builder
"""


class PromptBuilder:

    def __init__(self):

        self.system_prompt = """
You are IndianMiningGPT.

You are an expert assistant for:

- Indian Mining Laws
- DGMS Regulations
- MCDR
- MMDR Act
- Star Rating of Mines
- Environmental Compliance
- Mine Safety
- Sustainable Mining
- ESG in Mining

Instructions:

1. Use ONLY the provided context.

2. If the answer is not present in the context,
   reply:

   Information not found in the corpus.

3. Do not hallucinate.

4. Cite source files whenever possible.

5. Give concise and accurate answers.

6. If multiple sources support the answer,
   mention them.
"""

    def build(
        self,
        query,
        context
    ):

        prompt = f"""
{self.system_prompt}

==================================================
QUESTION
==================================================

{query}

==================================================
CONTEXT
==================================================

{context}

==================================================
ANSWER
==================================================
"""

        return prompt.strip()
