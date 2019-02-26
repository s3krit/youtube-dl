# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor
import base64

class EktoplazmIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?ektoplazm\.com/free-music/(?P<id>[a-zA-Z0-9\-]+)'
    _TEST = {
        'url': 'https://ektoplazm.com/free-music/mascalito-the-twilight-zone',
        'playlist':[
            {
                'md5': 'ba8b3753f3f6c9b6941221286a8742ec',
                'info_dict':{
                    'id': '1',
                    'ext': 'mp3',
                    'title': 'mascalito-rhythmical-disorder',
                }
            },
            {
                'md5': '3549a2b9fdba19084076ff198a517ae7',
                'info_dict':{
                    'id': '2',
                    'ext': 'mp3',
                    'title': 'mascalito-the-crack-between-the-world',
                }
            },
            {
                'md5': '9fd1bb2d55361317ba7258e323d69a20',
                'info_dict':{
                    'id': '3',
                    'ext': 'mp3',
                    'title': 'mascalito-filthy-summer',
                }
            },
            {
                'md5': 'fb76bca94e7e9ffc0743cddd7a1e23fb',
                'info_dict':{
                    'id': '4',
                    'ext': 'mp3',
                    'title': 'mascalito-mascalitos-mantra',
                }
            },
            {
                'md5': 'cbd5f19c12307c85845af54c3c461959',
                'info_dict':{
                    'id': '5',
                    'ext': 'mp3',
                    'title': 'mascalito-the-lecture',
                }
            },
            {
                'md5': '4f9f5ea048ea8042f442fce28d13b5b1',
                'info_dict':{
                    'id': '6',
                    'ext': 'mp3',
                    'title': 'mascalito-vs-shesha-fck1ng-shit-music',
                }
            }
        ],
        'info_dict': {
            'id': 'mascalito-the-twilight-zone',
            'title': 'Mascalito – The Twilight Zone',
            'thumbnail': r're:^https?://.*\.jpg$'
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        title = self._html_search_regex(r'<h1>(.+?)</h1>', webpage, 'title')
        thumbnail = self._search_regex(r'src="(.+?.jpg)" class="cover"', webpage, 'thumbnail')
        soundfiles = self._search_regex(r'soundFile:"(.+?)"', webpage, 'soundfiles')
        soundfiles += "=" * ((4 - len(soundfiles) % 4) % 4) #ugh
        files = base64.b64decode(soundfiles).decode('utf-8').split(',')
        track_id = 0
        entries = [
                {
                    'url': url,
                    'title': url.split('/')[-1].split('.')[0],
                    'id': str(i+1) # Even more ugh - no sensible IDs
                } for i,url in enumerate(files)
        ]

        return {
            '_type': 'playlist',
            'id': video_id,
            'title': title,
            'entries': entries,
            'thumbnail': thumbnail,
            'ext': 'mp3'
        }
