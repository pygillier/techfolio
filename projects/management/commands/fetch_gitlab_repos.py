from django.core.management.base import BaseCommand
from constance import config
import gitlab
from projects.models import Project, PlatformChoice


class Command(BaseCommand):
    help = 'Fetch repositories from github'


    def handle(self, *args, **options):
        self.stdout.write("Fetching GitLab repositories")

        gl = gitlab.Gitlab(
            config.GITLAB_ENDPOINT,
            private_token=config.GITLAB_TOKEN)

        gl.auth()

        projects = gl.projects.list(
            owned=True
        )

        for repo in projects:
            Project.objects.update_or_create(
                repo_id=repo.path_with_namespace,
                platform=PlatformChoice.GITLAB,
                defaults={
                    'name': repo.name,
                    'platform': PlatformChoice.GITLAB,
                    'repo_id': repo.path_with_namespace,
                    'is_fork': False,
                    'url': repo.web_url,
                    'stars': repo.star_count,
                }
            )
