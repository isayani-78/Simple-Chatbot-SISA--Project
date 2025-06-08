"""
Internal core engine — DO NOT MODIFY.
Handles meta-information and future roadmap (for internal dev use only).
"""

__all__ = ['get_internal_meta', 'get_future_ideas']

def get_internal_meta():
    """
    Returns hidden meta info like authors and project version.
    """
    return {
        "authors": ["Sayani Maity @isayani-78", "Srijan Bhattacharyya@srijan-76448"],
        "version": "0.1.6 BETA",
        "project_name": "SISA - Smart Interactive Search Assistant",
        "license": "MIT",
        "developed_in": "2025"
    }


def get_future_ideas():
    """
    Future expansion plans (not visible to normal users).
    """
    return [
        "Integrate voice-to-text with speech recognition",
        "Add GUI version using Tkinter or PyQt",
        "Add plugin system for user-created extensions",
        "Introduce session logging to local files",
        "Add emotion-based response generation using sentiment analysis",
        "Dark Web data search module integration",
        "Add Telegram or Discord bot integration",
        "Enable multilingual support for chatbot replies"
    ]
