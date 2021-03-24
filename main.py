from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
import logging

# create an instance of logger at a module level
logger = logging.getLogger(__name__)

try:
    from algoliasearch.search_client import SearchClient
except ImportError:
    import subprocess
    import sys
    import os

    subprocess.call([sys.executable, '-m', 'pip', 'install', '--user', '-r',
                     os.path.join(os.path.dirname(__file__), 'requirements.txt')])

    from algoliasearch.search_client import SearchClient


def get_description(hit):
    if hit["type"] == "episode":
        return "series: {} | In: {} | difficulty: {}".format(hit["series"], hit["taxonomy"], hit["difficulty"])
    elif hit["type"] == "series":
        return "episodes: {} | In: {} | difficulty: {}".format(hit["episode_count"], hit["taxonomy"], hit["difficulty"])
    else:
        return ""

class LaracastsExtension(Extension):

    def __init__(self):
        super(LaracastsExtension, self).__init__()

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        agolia = SearchClient.create("1Z405N45FC", "6c44626a6a8c21778291dc05232905e6")
        self.index = agolia.init_index("lessons")


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        description = "Type in your query and press Enter..."

        url = "https://laracasts.com"
        extensionResults = []
        if event.get_argument() is not None:
            results = extension.index.search(
                event.get_argument(), {"hitsPerPage": 10}
            )

            for hit in results["hits"]:
                extensionResults.append(ExtensionResultItem(
                    icon='icons/laracasts.svg',
                    name=hit["title"],
                    description=get_description(hit),
                    on_enter=OpenUrlAction(url + hit["path"])
                ))
        if len(extensionResults) == 0:
            extensionResults.append(ExtensionResultItem(
                icon='icons/laracasts.svg',
                name="Search Laracasts",
                description=description,
                on_enter=OpenUrlAction(url)
            ))

        return RenderResultListAction(extensionResults)


if __name__ == '__main__':
    LaracastsExtension().run()
