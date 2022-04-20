# Scrapy settings for lmparser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lmparser'
IMAGES_STORE = 'photos'

ITEM_PIPELINES = {
    'lmparser.pipelines.LmparserPipeline': 300,
    'lmparser.pipelines.LmPhotosPipeline': 200,
}

SPIDER_MODULES = ['lmparser.spiders']
NEWSPIDER_MODULE = 'lmparser.spiders'
LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'  # DEBUG, INFO, WARNING, ERROR (for regular errors), CRITICAL (for critical errors (highest severity)

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'lmparser (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 ' \
             'Safari/537.36 '

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
DOWNLOAD_DELAY = 1.5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }
# DEFAULT_REQUEST_HEADERS = {
#     'cookie': 'dtCookie=v_4_srv_3_sn_64D3C58B35B7CF6C0A607FF5B09ACA76_perc_1_ol_1_app-3Ab82b63450c1d92de_0; disp_plp_promo_ab=A; ggr-widget-test=0; flowbox-gallery-pdp=0; _regionID=34; iap.uid=f1288b95685a4ef18664ff7b2f83442e; _gcl_au=1.1.764600238.1650388816; dmpuid=cjj4CtThTFyFbvaANYHB-g; dmpuid-legacy=cjj4CtThTFyFbvaANYHB-g; _gaexp=GAX1.2.ouICWlkpTuKpvosrUFwQ2g.19166.1!mAlGV6AUTqahU-DeeZgLtQ.19183.1; x-api-option=default; _ga=GA1.2.690388904.1650388818; _gid=GA1.2.39565434.1650388818; aplaut_distinct_id=2Yt3wJDgpXRa; lastConfirmedRegionID=34; uxs_uid=fc4e8810-c004-11ec-a6da-ede318f9f00f; cookie_accepted=true; user-geolocation=0%2C0; GACookieStorage=GA1.2.690388904.1650388818; X-API-Experiments-sub=B; qrator_ssid=1650396828.048.t8U0dLPzZ1VfZevu-1cvvlk1s19p5aj7e3673aimr477lekl9; qrator_jsid=1650396826.810.6RQYAZ2u2GcHgJTl-p7u9nfk2qk3m5p769392v5ha2kpd4f2o; recently_viewed=90005561%2C84771081%2C90134085%2C82467040; storageForShopListActual=true; _dc_gtm_UA-20946020-1=1'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'lmparser.middlewares.LmparserSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'lmparser.middlewares.LmparserDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'lmparser.pipelines.LmparserPipeline': 300,
# }
# ITEM_PIPELINES = {
#     'lmparser.pipelines.LmparserPipeline': 300,
#     'lmparser.pipelines.LmPhotosPipeline': 200
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
