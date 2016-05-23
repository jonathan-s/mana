from pelican import signals
from itertools import chain


def add_blog_posts(generator):
    numentries = generator.settings.get('WIDGET_POST_MAX', 3)
    posts = []

    for article in chain(generator.articles, generator.drafts):
        if article.category.slug == 'blogg':
            posts.append(article)

        if len(posts) >= numentries:
            break
    generator.blog_articles = posts
    generator._update_context(('blog_articles',))


def register():
    signals.article_generator_finalized.connect(add_blog_posts)
