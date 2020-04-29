
#%%
import re
import youtube_dl
import os
import time
import datetime
import subprocess
import locale
import codecs

f = open('output_0.html', 'r')
page = f.read()
f.close()
#print(page)
#<script id="js-live-data" data-json="{&quot;high_point_gift_list&quot;:[],&quot;live_res&quot;:{},&quot;is_only_hls&quot;:0,&quot;tweet_url&quot;:&quot;&quot;,&quot;support_users&quot;:null,&quot;support_data&quot;:null,&quot;telop&quot;:&quot;&quot;,&quot;is_login&quot;:0,&quot;can_comment&quot;:1,&quot;live_id&quot;:0,&quot;has_regular_event&quot;:0,&quot;background_image_url&quot;:&quot;&quot;,&quot;ranking&quot;:{&quot;live_ranking&quot;:[]},&quot;broadcast_key&quot;:&quot;d869ae8f216cc78d58c218f0be5fd9f2e027e4d222d430119bad7bd0f5e8e223&quot;,&quot;online_user_num&quot;:&quot;0&quot;,&quot;is_twitter_auth&quot;:0,&quot;regular_event_data&quot;:null,&quot;nsta_owner&quot;:0,&quot;is_enquete&quot;:0,&quot;get_daily_bonus&quot;:0,&quot;room&quot;:{&quot;room_banner_file_type1&quot;:&quot;png&quot;,&quot;content_region_permission&quot;:&quot;1&quot;,&quot;banner_image_url1&quot;:&quot;https://image.showroom-live.com/showroom-prod/image/room/8722e9e9445b675e9943a19973551e414370a449008e8640d37b0c66a72e94e6/banner_1.png?v=1583075113&quot;,&quot;room_style_id&quot;:&quot;0&quot;,&quot;last_live_id&quot;:&quot;9256362&quot;,&quot;is_online&quot;:&quot;0&quot;,&quot;performer_name&quot;:null,&quot;follower_num&quot;:&quot;5514&quot;,&quot;banner_url2&quot;:&quot;https://fortunemusic.jp/227_202002/&quot;,&quot;archive_not_delete&quot;:&quot;0&quot;,&quot;performer_hometown&quot;:&quot;0&quot;,&quot;room_type&quot;:&quot;1&quot;,&quot;is_free&quot;:&quot;0&quot;,&quot;no_listing&quot;:&quot;0&quot;,&quot;is_official&quot;:&quot;1&quot;,&quot;regular_event_id&quot;:&quot;0&quot;,&quot;organizer_id&quot;:&quot;1658&quot;,&quot;is_first_live&quot;:&quot;0&quot;,&quot;image_l&quot;:&quot;https://image.showroom-live.com/showroom-prod/image/room/cover/8722e9e9445b675e9943a19973551e414370a449008e8640d37b0c66a72e94e6_l.jpeg?v=1583075113&quot;,&quot;image_s&quot;:&quot;https://image.showroom-live.com/showroom-prod/image/room/cover/8722e9e9445b675e9943a19973551e414370a449008e8640d37b0c66a72e94e6_s.jpeg?v=1583075113&quot;,&quot;account_id&quot;:&quot;&quot;,&quot;genre_id&quot;:&quot;102&quot;,&quot;cover_image_file_type&quot;:&quot;jpeg&quot;,&quot;level&quot;:&quot;39&quot;,&quot;youtube_id&quot;:&quot;J9JQrg1ugsk&quot;,&quot;updated_at&quot;:&quot;1583075113&quot;,&quot;image_ss&quot;:&quot;https://image.showroom-live.com/showroom-prod/image/room/cover/8722e9e9445b675e9943a19973551e414370a449008e8640d37b0c66a72e94e6_ss.jpeg?v=1583075113&quot;,&quot;last_lived_at&quot;:&quot;1586926818&quot;,&quot;room_url_key&quot;:&quot;digital_idol_15&quot;,&quot;room_description&quot;:&quot;22/7(ナナブンノニジュウニ)の武田愛奈(たけだあいな)と申します。皆様、宜しくお願いいたします。&quot;,&quot;status&quot;:&quot;1&quot;,&quot;image_m&quot;:&quot;https://image.showroom-live.com/showroom-prod/image/room/cover/8722e9e9445b675e9943a19973551e414370a449008e8640d37b0c66a72e94e6_m.jpeg?v=1583075113&quot;,&quot;performer_description&quot;:null,&quot;next_live&quot;:&quot;TBD&quot;,&quot;popularity_point&quot;:&quot;3832316&quot;,&quot;created_at&quot;:&quot;1481714462&quot;,&quot;room_image_file_type&quot;:&quot;png&quot;,&quot;room_banner_file_type2&quot;:&quot;jpeg&quot;,&quot;banner_image_url2&quot;:&quot;https://image.showroom-live.com/showroom-prod/image/room/8722e9e9445b675e9943a19973551e414370a449008e8640d37b0c66a72e94e6/banner_2.jpeg?v=1583075113&quot;,&quot;room_name&quot;:&quot;武田愛奈　22/7(ナナブンノニジュウニ)&quot;,&quot;birthday&quot;:&quot;0&quot;,&quot;current_support_id&quot;:&quot;0&quot;,&quot;twitter_text&quot;:&quot;&quot;,&quot;capacity&quot;:&quot;0&quot;,&quot;archive_flag&quot;:&quot;0&quot;,&quot;recommend_comment_open_status&quot;:&quot;1&quot;,&quot;banner_url1&quot;:&quot;http://227-game.com&quot;,&quot;room_id&quot;:&quot;87759&quot;},&quot;gift_list&quot;:[],&quot;is_owner&quot;:0,&quot;has_support&quot;:0,&quot;is_live&quot;:0,&quot;daily_bonus_item_id&quot;:0,&quot;has_event&quot;:0,&quot;event_data&quot;:null,&quot;broadcast_port&quot;:8080,&quot;my_data&quot;:{&quot;avatar_id&quot;:null,&quot;live_rank&quot;:0,&quot;next_level_point&quot;:0,&quot;no_confirm_gifting_point&quot;:null,&quot;locale&quot;:null,&quot;next_fan_level&quot;:0,&quot;gold&quot;:0,&quot;badge&quot;:0,&quot;fan_level&quot;:1,&quot;is_tutorial&quot;:0,&quot;name&quot;:null,&quot;avatar_url&quot;:null,&quot;image_s&quot;:null,&quot;current_level_point&quot;:0,&quot;account_id&quot;:null,&quot;live_user_key&quot;:null,&quot;contribution_point&quot;:0,&quot;user_id&quot;:0,&quot;do_notify&quot;:0},&quot;ec_config&quot;:{&quot;sales_available&quot;:0,&quot;created_at&quot;:0,&quot;present_available&quot;:0,&quot;updated_at&quot;:0,&quot;room_id&quot;:&quot;87759&quot;},&quot;broadcast_host&quot;:&quot;online.showroom-live.com&quot;,&quot;live_user_key&quot;:null,&quot;new_streaming&quot;:1,&quot;premium_room_type&quot;:0,&quot;tweet_default&quot;:&quot;武田愛奈　22/7(ナナブンノニジュウニ) Broadcasting! #SHOWROOM&quot;,&quot;room_id&quot;:&quot;87759&quot;,&quot;enquete_data&quot;:null}"></script>
pattern = re.compile('<script id="js-live-data"(.*?)"></script>')
result = re.search(pattern, page)
m3u8_url = result.group(1)
pattern = re.compile('<title>(.*?) - SHOWROOM</title>')
result = re.search(pattern, page)
filename = result.group(1)
print(time.time())
filename = filename + '_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
print(filename)
"""
command = "ping www.baidu.com"#可以直接在命令行中执行的命令
r = os.popen(command)
info = r.readlines()
print("INFO:")
for line in info: #按行遍历
    line = line.strip("\r\n")
    print(line)
# %%
"""