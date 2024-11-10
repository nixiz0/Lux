from CONFIG import LANGUAGE


def pause_running():
    return "Système mis en pause" if LANGUAGE == 'fr' else "System paused"
