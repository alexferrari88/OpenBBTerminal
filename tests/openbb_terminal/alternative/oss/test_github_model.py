# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.alternative.oss import github_model


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [
            ("User-Agent", None),
            ("Authorization", "MOCK_AUTHORIZATION"),
        ],
    }


@pytest.mark.asyncio
@pytest.mark.vcr
@pytest.mark.parametrize(
    "repo",
    [("openbb-finance/openbbterminal")],
)
async def test_get_repo_summary(repo, recorder):
    df = await github_model.get_repo_summary(
        repo=repo,
    )
    recorder.capture(df)


@pytest.mark.asyncio
@pytest.mark.vcr
@pytest.mark.parametrize(
    "repo",
    [("openbb-finance/openbbterminal")],
)
async def test_get_stars_history(repo, recorder):
    df = await github_model.get_stars_history(
        repo=repo,
    )
    recorder.capture(df)


@pytest.mark.asyncio
@pytest.mark.vcr
@pytest.mark.parametrize(
    "sortby,top,categories",
    [("stars", 10, "")],
)
async def test_get_top_repos(sortby, top, categories, recorder):
    df = await github_model.get_top_repos(sortby, top, categories)
    recorder.capture(df)
