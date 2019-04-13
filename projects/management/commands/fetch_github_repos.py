from django.core.management.base import BaseCommand
from constance import config
from github3 import login
from projects.models import Project, PlatformChoice


class Command(BaseCommand):
    help = 'Fetch repositories from github'

    def handle(self, *args, **options):
        self.stdout.write("Fetching GitHub repositories")

        gh = login(token=config.GITHUB_TOKEN)

        me = gh.me()

        for repo in gh.repositories_by(username=me.login):
            repo = repo.refresh()
            Project.objects.update_or_create(
                repo_id=repo.full_name,
                platform=PlatformChoice.GITHUB,
                defaults={
                    'name': repo.name,
                    'platform': PlatformChoice.GITHUB,
                    'repo_id': repo.full_name,
                    'is_fork': repo.fork,
                    'url': repo.html_url,
                    'releases_url': repo.downloads_url,
                    'parent_url': repo.parent.html_url if repo.fork else None,
                    'stars': repo.stargazers_count,
                }
            )
