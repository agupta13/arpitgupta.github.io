source "https://rubygems.org"

# Jekyll 4.x – compatible with Ruby >= 3.1
gem "jekyll", "~> 4.3"

# Required since Ruby 3.0 removed the bundled webrick
gem "webrick", "~> 1.8"

# Windows directory watcher
gem "wdm", "~> 0.1.0" if Gem.win_platform?

# Plugins (must match the plugins: list in _config.yml)
group :jekyll_plugins do
  gem "jekyll-paginate", "~> 1.1"
  gem "jekyll-sitemap", "~> 1.4"
  gem "jekyll-gist", "~> 1.5"
  gem "jekyll-feed", "~> 0.17"
  gem "jekyll-redirect-from", "~> 0.16"
end
