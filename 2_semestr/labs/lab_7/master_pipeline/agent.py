from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.parallel_agent import ParallelAgent
from google.adk.agents.loop_agent import LoopAgent

# ==========================================
# 1. PARALLEL: Збір даних з різних джерел
# ==========================================
ai_researcher = Agent(
    name="ai_researcher", 
    model="gemini-2.5-flash", 
    instruction="Ти дослідник ШІ. Знайди і напиши 2 речення про головний тренд штучного інтелекту."
)

cyber_researcher = Agent(
    name="cyber_researcher", 
    model="gemini-2.5-flash", 
    instruction="Ти дослідник кібербезпеки. Напиши 2 речення про головні загрози кібербезпеки."
)

data_gathering_stage = ParallelAgent(
    name="data_gathering",
    sub_agents=[ai_researcher, cyber_researcher]  # ВИПРАВЛЕНО: sub_agents замість agents
)

# ==========================================
# 2. LOOP: Ітеративне покращення тексту
# ==========================================
def approve_quality(text: str) -> dict:
    """Перевіряє, чи достатньо великий текст для фінального звіту."""
    if len(text) > 300:
        return {"status": "success", "action": "exit_loop", "message": "Якість чудова, цикл завершено."}
    return {"status": "continue", "message": "Текст занадто короткий. Додай більше деталей та висновок."}

editor_agent = Agent(
    name="editor",
    model="gemini-2.5-flash",
    instruction="Ти головний редактор. Твоє завдання — розширити текст, зробити його професійним та додати висновок. Використовуй інструмент approve_quality для перевірки.",
    tools=[approve_quality]
)

quality_improvement_stage = LoopAgent(
    name="quality_loop",
    sub_agents=[editor_agent],  # ВИПРАВЛЕНО: sub_agents замість agent
    max_iterations=3
)

# ==========================================
# 3. SEQUENTIAL: Об'єднання всього у конвеєр
# ==========================================
analyzer_agent = Agent(
    name="analyzer",
    model="gemini-2.5-flash",
    instruction="Проаналізуй дані від дослідників і напиши чорновий звіт (один абзац)."
)

# Root Agent (Оркестратор)
root_agent = SequentialAgent(
    name="master_pipeline",
    sub_agents=[  # ВИПРАВЛЕНО: sub_agents замість agents
        data_gathering_stage,
        analyzer_agent,
        quality_improvement_stage
    ]
)