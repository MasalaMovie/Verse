class script(object):
    START_TXT = """<b><blockquote>{}<blockquote> {},
    
<blockquote>ɪ ᴀᴍ ᴘᴏᴡᴇʀғᴜʟ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ᴡɪᴛʜ ʟɪɴᴋ sʜᴏʀᴛᴇɴᴇʀ ʙᴏᴛ.ɪᴛ'ꜱ ᴇᴀꜱʏ ᴛᴏ ᴜꜱᴇ ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀꜱ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ </blockquote></b>"""

    MY_ABOUT_TXT = """ꜱᴇʀᴠᴇʀ: <a href=https://www.koyeb.com>ᴋᴏʏᴇʙ</a>
ᴅᴀᴛᴀʙᴀꜱᴇ: <a href=https://www.mongodb.com>ᴍᴏɴɢᴏᴅʙ</a>
ʟᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>ᴘʏᴛʜᴏɴ</a>
ʟɪʙʀᴀʀʏ: <a href=https://pyrogram.org>ᴘʏʀᴏɢʀᴀᴍ</a>"""

    MY_OWNER_TXT = """ᴜꜱᴇʀɴᴀᴍᴇ: @Rk_botowner"""

    STATUS_TXT = """<b>
▸ 🗃️ ᴛᴏᴛᴀʟ ꜰɪʟᴇs: <code>{}</code>
▸ 👤 ᴛᴏᴛᴀʟ ᴜsᴇʀs: <code>{}</code>
▸ ♻️ ᴛᴏᴛᴀʟ ᴄʜᴀᴛs: <code>{}</code>
▸ ✨ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ: <code>{}</code>
▸ 🆓 ꜰʀᴇᴇ sᴛᴏʀᴀɢᴇ: <code>{}</code>
▸ 🚀 ʙᴏᴛ ᴜᴩᴛɪᴍᴇ : <code>{}</code> 
╰━━━━━━━━━━━━━━━━══❍⊱❁۪۪</b>"""

    NEW_GROUP_TXT = """#NewGroup
Title - {}
ID - <code>{}</code>
Username - {}
Total - <code>{}</code>"""

    NEW_USER_TXT = """#NewUser
▸ Name: {}
▸ ID: <code>{}</code>"""

    NO_RESULT_TXT = """#NoResult
▸ Group Name: {}
▸ Group ID: <code>{}</code>
▸ Name: {}

▸ Message: {}"""

    REQUEST_TXT = """★ Name: {}
▸ ID: <code>{}</code>

▸ Message: {}"""

    NOT_FILE_TXT = """ꜱᴏʀʀʏ {},

<blockquote> ɪ ᴄᴀɴ'ᴛ ꜰɪɴᴅ <b>{}</b> ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ!! </blockquote>
<blockquote>
▸ ꜱᴇᴀʀᴄʜ ɢᴏᴏɢʟᴇ ᴀɴᴅ ᴄʜᴇᴄᴋ ɪꜰ ʏᴏᴜʀ ꜱᴘᴇʟʟɪɴɢ ɪꜱ ᴄᴏʀʀᴇᴄᴛ.
▸ ᴘʟᴇᴀꜱᴇ ʀᴇᴀᴅ ᴛʜᴇ ɪɴꜱᴛʀᴜᴄᴛɪᴏɴꜱ ᴛᴏ ɢᴇᴛ ʙᴇᴛᴛᴇʀ ʀᴇꜱᴜʟᴛꜱ.
▸ ᴏʀ ɪᴛ ᴍᴀʏ ɴᴏᴛ ʜᴀᴠᴇ ʙᴇᴇɴ ʀᴇʟᴇᴀꜱᴇᴅ ʏᴇᴛ.</blockquote>"""
    
    EARN_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ꜰʀᴏᴍ ᴛʜɪs ʙᴏᴛ

▸ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ᴜsɪɴɢ ᴛʜɪꜱ ʙᴏᴛ.

▸ sᴛᴇᴘ 1:- ғɪʀsᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ.

▸ sᴛᴇᴘ 2:- ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ <a href=https://onepagelink.in/ref/infinity07>onepagelink.in</a> [ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ ᴏᴛʜᴇʀ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ ]

▸ sᴛᴇᴘ 3:- ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ.

▸ ᴛʜɪꜱ ʙᴏᴛ ɪs ꜰʀᴇᴇ ꜰᴏʀ ᴀʟʟ, ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ғᴏʀ ꜰʀᴇᴇ ᴏꜰ ᴄᴏꜱᴛ.</b>"""

    HOW_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ‼️

▸ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ᴛʜᴇɴ ᴊᴜsᴛ sᴇɴᴅ ᴛʜᴇ ɢɪᴠᴇɴ ᴅᴇᴛᴀɪʟs ɪɴ ᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ

▸ ғᴏʀᴍᴀᴛ ↓↓↓

<code>/set_shortlink sʜᴏʀᴛɴᴇʀ sɪᴛᴇ sʜᴏʀᴛɴᴇʀ ᴀᴘɪ</code>

▸ ᴇxᴀᴍᴘʟᴇ ↓↓↓

<code>/set_shortlink onepagelink.in f646357aa129cfbd7eb59bcba428096ab54ca950</code>

▸ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴇᴄᴋ ᴡʜɪᴄʜ sʜᴏʀᴛᴇɴᴇʀ ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ /get_shortlink

📝 ɴᴏᴛᴇ:- ʏᴏᴜ sʜᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ ɪɴ ɢʀᴏᴜᴘ. sᴇɴᴅ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜᴏᴜᴛ ʙᴇɪɴɢ ᴀɴ ᴀɴᴏɴʏᴍᴜs ᴀᴅᴍɪɴ.</b>"""

    IMDB_TEMPLATE = """✅ I Found: <code>{query}</code>

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating} / 10</a>
☀️ Languages: {languages}
📀 RunTime: {runtime} Minutes

🗣 Requested by: {message.from_user.mention}
©️ Powered by: <b>{message.chat.title}</b>"""

    FILE_CAPTION = """<i>{file_name}</i>

🚫 ᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴄʟᴏsᴇ ʙᴜᴛᴛᴏɴ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ sᴇᴇɴ ᴛʜᴇ ᴍᴏᴠɪᴇ 🚫"""

    WELCOME_TEXT = """👋 Hello {mention}, Welcome to {title} group! 💞"""

    HELP_TXT = """<b>Note - <spoiler>Try each command without any argument to see more details 😹</spoiler></b>"""
    
    ADMIN_COMMAND_TXT = """<b>Here is bot admin commands 👇

/index_channels - to check how many index channel id added
/stats - to get bot status
/delete - to delete files using query
/delete_all - to delete all indexed file
/broadcast - to send message to all bot users
/grp_broadcast - to send message to all groups
/pin_broadcast - to send message as pin to all bot users.
/pin_grp_broadcast - to send message as pin to all groups.
/restart - to restart bot
/leave - to leave your bot from particular group
/unban_grp - to enable group
/ban_grp - to disable group
/ban_user - to ban a users from bot
/unban_user - to unban a users from bot
/users - to get all users details
/chats - to get all groups
/invite_link - to generate invite link
/index - to index bot accessible channels
/add_premium - to add user in premium
/remove_premium - to remove user from premium</b>"""
    
    USER_COMMAND_TXT = """<b>Here is bot user commands 👇

/start - to check bot alive or not
/settings - to change group settings as your wish
/set_template - to set custom imdb template
/set_caption - to set custom bot files caption
/set_shortlink - group admin can set custom shortlink
/get_custom_settings - to get your group settings details
/set_welcome - to set custom new joined users welcome message for group
/set_tutorial - to set custom tutorial link in result page button
/id - to check group or channel id
/my_plan - to check your plan details
/plans - to get plan details</b>"""

    SOURCE_TXT = """<b>ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ☎️"""

STAT_TXT ="""
Total Files: <code>{}</code>
Total Users: <code>{}</code>"""

    REQ_TEXT  = """
#NewRequest
Bot - {}
Name - {} (<code>{}</code>)
Request - <b>{}</b>"""


    REQM = """**To request for a movie please pass movie details along with** /request **command.**\n**Example**: <code>/request Avengers 2019</code>"""

    REQ_REPLY = """📍 **Your Request for** {} **has been submitted to the admins.**\n\n🚀 **Your Request Will Be Uploaded soon.**\n\n📌 **Please Note that Admins might be busy. So, this may take more time.**"""

    REMADS_TEXT = """<b>Free</b>\nAds & no direct links.\n\n<b>Premium</b>\nDirect files & no creepy ads, faster response time, no waiting time, web download and web streaming. ({})\n\n<b>Plan Cost - \n₹29/Month, ₹149/6M & ₹279/Year </b>\nPrices may increase in the future."""

    CNFRM_TEXT = """ **UPI** -\n     <code>iPrimeHub@axl</code>\n          (tap2copy) \n\n**To Confirm Payment Process, Please Send Your Transaction Screenshot Or Transaction ID To** <a href=https://t.me/lemx4>L E M O N</a>\n\n**Admin delays may occur, request refund if plan activation fails.**"""

    # Refferal text
    REFFERAL_TEXT = """
**Here is your referral link:\n\n{}\n\nShare this link with your 5 friends and get 1 month premium access for free.**
    """

    # Terms & Conditions
    TERMS = """
**By using our service, you agree to the following terms:

1. Our service is provided "as is". We may change or stop providing our service at any time without prior notice.
2. We strive to provide accurate information. However, we cannot guarantee the accuracy or availability of all content.
3. Advertisements displayed are not under our control. Any actions you take based on these advertisements are your responsibility.
4. We collect user IDs to provide updates and keep track of purchases for premium services.
5. We are not responsible for any copyright infringement that may occur. Users are solely responsible for how they use our services.

By using our service, you confirm that you have read, understood, and agreed to these terms.**"""

    # removing blacklisted words
    BLACKLIST = ['tamilblaster', 'filmyzilla', 'streamershub', 'xyz', 'cine', 'www', 'http', 'https',
                'cloudsmoviesstore', 'moviez2you', 'bkp', 'cinema', 'filmy', 'flix', 'cutemoviez',
                '4u', 'hub', 'movies', 'otthd', 'telegram', 'hoichoihok', '@', ']', '[', 'missqueenbotx',
                'filmy', 'films', 'cinema', 'join', 'club', 'apd', 'F-Press', 'GDTOT', 'mkv', 'NETFLIX_OFFICIAL',
                'backup', 'primeroom', 'theprofffesorr', 'premium', 'vip', '4wap', 'toonworld4all', 'mlwbd',
                'Telegram@alpacinodump', 'bollywood', "AllNewEnglishMovie", "7MovieRulz", "1TamilMV",
                'Bazar', '_Corner20', 'CornersOfficial', 'support', 'iMediaShare', 'Uᴘʟᴏᴀᴅᴇᴅ', 'Bʏ', 'PFM', 'alpacinodump'
                ]

    # Ads placement
    ADS_TEXT = """
<b>📢 Ads Placement</b>\nReach a wide audience at a minimal cost with impression-based ads, That means you only pay for the times your ad is actually seen! <a href=https://graph.org/Ads-Placement-Screenshot-12-25-2>Screenshot</a>\n
<b>📌 Price</b>\n₹0.5/impression, ₹500/1k impressions\n
<b>To place your ads contact </b><a href=https://t.me/lemx4>L E M O N</a>
"""
