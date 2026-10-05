"""
Test-Coverage Agent — same ReAct graph shape as the Style Agent (Phase 3),
built via react_agent_factory, bound to the test-coverage detector tool instead.

Responsible ONLY for test coverage feedback (whether tests were added/updated,
test framework detection, test completeness). Must NOT comment on style or
security — those belong to the other specialist agents.
"""
from langchain_core.tools import tool

from app.agents.react_agent_factory import build_single_tool_agent
from app.tools.test_detector import check_test_coverage

TEST_COVERAGE_AGENT_SYSTEM_PROMPT = """You are a Test Coverage Reviewer, one specialist on a code review team.

Your ONLY job is checking test coverage: whether tests were added or updated for new or
modified functionality, whether test frameworks are used appropriately, and test completeness.
You do NOT comment on style or security - other specialists on the team own those, and
commenting outside your lane creates noise.

Always call the check_test_coverage_tool on the diff before writing feedback - do not guess at
test coverage from reading the diff yourself.

After seeing the tool result, write your review as a short PR comment (1-3 sentences, like a real
human reviewer would leave). If adequate tests were added, say so briefly. If tests are missing
or insufficient, clearly state what needs tests instead of inventing feedback.

If the tool reports that this language is not supported, say so plainly
(e.g. "Test coverage checking isn't available for this language yet") - do NOT claim test coverage
is adequate, since that was never actually checked.
"""


@tool
def check_test_coverage_tool(diff_hunk: str, old_file: str = "", lang: str = "py") -> str:
    """Check a code diff for test coverage: whether test files are included,
    test framework detection, and production-to-test file ratio. Call this before
    giving any test coverage feedback on a diff."""
    result = check_test_coverage(diff_hunk, old_file=old_file, lang=lang)
    if result.get("unsupported_language"):
        return (
            f"TEST COVERAGE CHECK NOT AVAILABLE for language '{lang}'. This is not "
            "the same as 'no issues found' - the check was never performed. "
            "Do not claim test coverage is adequate; state plainly that test coverage "
            "checking isn't supported for this language."
        )
    output = result["summary"]
    if result.get("recommendation"):
        output += f"\n\nRecommendation:\n{result['recommendation']}"
    return output


def run_test_coverage_review(diff_hunk: str, old_file: str = "", lang: str = "py", session_id: str = None) -> str:
    """Run the Test Coverage Agent on one diff and return its final review comment."""
    run = build_single_tool_agent(TEST_COVERAGE_AGENT_SYSTEM_PROMPT, check_test_coverage_tool)

    user_prompt = f"""Review this diff for TEST COVERAGE only.

Language: {lang}

Original file (context, may be truncated):
{old_file[:500]}

Diff:
{diff_hunk}
"""
    return run(user_prompt, session_id=session_id)
