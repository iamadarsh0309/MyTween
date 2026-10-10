from zenml import step


@step
def get_or_create_user(user_full_name: str) -> str:
    """
    Get an existing user or create a new one.

    For now, we simply return the user's name.
    Database persistence will be implemented later.
    """
    print(f"Getting or creating user: {user_full_name}")

    return user_full_name


@step
def crawl_links(user: str, links: list[str]) -> None:
    """
    Crawl the provided links and collect the user's digital data.

    Actual crawling/storage logic will be implemented later.
    """
    print(f"Crawling {len(links)} links for user: {user}")

    for link in links:
        print(f"Crawling: {link}")