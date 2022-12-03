{
  "ru":
  [
    {
      "apteka.ru": {
        "url": "https://api.apteka.ru/Auth/Auth_Code?cityUrl=moskva",
        "json": "{'phone': '*phone()*' , 'u': 'U'}",
        "headers": {
          "Accept": "*/*",
          "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
          "Access-Control-Request-Headers": "authorization,content-type",
          "Access-Control-Request-Method": "POST",
          "Connection": "keep-alive",
          "Host": "api.apteka.ru",
          "Origin": "https://apteka.ru",
          "Referer": "https://apteka.ru/",
          "Sec-Fetch-Dest": "empty",
          "Sec-Fetch-Mode": "cors",
          "Sec-Fetch-Site": "same-site",
          "User-Agent": ""
        },
        "response": 200,
        "timeout": 120
      },
      "magnit": {
        "url": "https://new.moy.magnit.ru/local/ajax/login/",
        "data": "{'phone': '*+phone*', 'ksid': 'ee191257-a4fe-4e39-9f0f-079c7f721eee_0'}",
        "response": "json",
        "timeout": 120
      },
      "telegram": {
        "url": "https://my.telegram.org/auth/send_password",
        "data": "{'phone': '*+phone*'}",
        "response": 200,
        "timeout": 120
      },
      "citi_link": {
        "url": "https://www.citilink.ru/registration/confirm/phone/*phone*/",
        "data": "{'phone': '*phone*', 'ret': '1', 'smsRepeatDelay': '60', 'smsRepeatsDelay': '60', 'smsRepeatsLimit': '5', 'smsRequestToken': '0220c808-b9fb-408c-a383-897cd658989f'}",
        "response": 200,
        "timeout": 100
      },
      "akbarsa": {
        "url": "https://www.akbars.ru/api/PhoneConfirm/",
        "json": "{'phoneNumber': *phone*}",
        "response": 200,
        "timeout": 300
      },
      "yota": {
        "url": "https://bmp.tv.yota.ru/api/v10/auth/register/msisdn",
        "json": "{'msisdn': '*phone*', 'password': '123456'}",
        "cookies": "https://tv.yota.ru/",
        "response": 201,
        "timeout": 60
      },
      "b_apteka": {
        "url": "https://b-apteka.ru/lk/send_confirm_code",
        "json": "{'phone': '*phone*'}",
        "headers": {
          "X-Requested-With": "XMLHttpRequest",
          "Connection": "keep-alive",
          "Pragma": "no-cache",
          "Cache-Control": "no-cache",
          "Accept-Encoding": "gzip, deflate, br",
          "User-Agent": "",
          "DNT": "1"
        },
        "response": 200,
        "timeout": 60
      },
      "pochtabank": {
        "url": "https://my.pochtabank.ru/dbo/registrationService/ib/phoneNumber",
        "json": "{'confirmation': 'send', 'phone': '*phone()*'}",
        "response": 200,
        "timeout": 120
      },
      "mt_free": {
        "url": "https://cabinet.wi-fi.ru/api/auth/by-sms",
        "data": "{'msisdn': '*mtfree*', 'g-recaptcha-response': ''}",
        "headers": {
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
          "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
          "App-ID": "cabinet",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive",
          "User-Agent": ""
        },
        "response": "json",
        "timeout": 180
      },
      "megafon.tv": {
        "url": "https://bmp.megafon.tv/api/v10/auth/register/msisdn",
        "json": "{'msisdn':'*+phone*', 'password':'123456'}",
        "response": 201,
        "timeout": 600,
        "cookies": "https://megafon.tv/"
      },
      "moezdorovie": {
        "url": "https://moezdorovie.ru/rpc/?method=auth.GetCode",
        "json": "{'jsonrpc':'2.0','id':40,'method':'auth.GetCode','params':{'phone':'*-phone*','mustExist':false, 'sendRealSms':true}}",
        "response": 200,
        "timeout": 300
      },
      "totopizza": {
        "url": "https://api.totopizza.ru/graphql",
        "json": "{\"operationName\":\"requestPhoneCodeAuth\",\"query\":\"\\n  mutation requestPhoneCodeAuth($telephone:String!) {\\n    requestPhoneCodeAuth(telephone:$telephone)\\n  }\\n\",\"variables\":{\"telephone\":\"*phone2*\"}}",
        "response": 200,
        "timeout": 60
      },
      "zdesapteka": {
        "url": "https://zdesapteka.ru/bitrix/services/main/ajax.php?action=zs:main.ajax.AuthActions.sendAuthCode",
        "data": "{'userPhone': '*phone()*', 'SITE_ID': 's1', 'sessid': ''}",
        "response": 200,
        "timeout": 60,
        "cookies": "https://zdesapteka.ru/"
      },
      "stockmann": {
        "url": "https://stockmann.ru/ajax/?controller=user&action=registerUser&surname=Popovich&name=Oleg&phone=*phone3*&email=rgeaefs@gmail.com&password=123456&password_confirm=123456",
        "response": 200,
        "timeout": 600
      },
      "SberUslugi": {
        "url": "https://sberuslugi.ru/api/v1/user/secret",
        "data": "{'phone': '*phone()*'}",
        "response": 200,
        "timeout": 180
      },
      "victoria": {
        "url": "https://new.victoria-group.ru/api/v2/manzana/Identity/RequestAdvancedPhoneEmailRegistration",
        "response": 200,
        "timeout": 60
      },
      "sunlight": {
        "url": "https://api.sunlight.net/v3/customers/authorization/",
        "json": "{'phone':'*phone*'}",
        "response": 200,
        "timeout": 30,
        "cookies": "https://sunlight.net/profile/login/?next_encoded=Lw=="
      },
      "ok.ru": {
        "url": "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
        "data": "{'st.r.phone': '*phone*'}",
        "response": 200,
        "timeout": 60,
        "cookies": "https://ok.ru/"
      },
      "citystar": {
        "url": "https://citystarwear.com/bitrix/templates/bspc/php/bs.auth.sms/templates/pc/handlers.php",
        "data": "{'hdlr': 'bsSendCodeAuth','bshsmsk': 'h5Plm22xoaFs9YTp', 'phone': '*-phone*', 'xemail': '', 'xphone': ''}",
        "response": 200,
        "timeout": 180
      },
      "beerlogapizza": {
        "url": "https://smsc.ru/sys/send.php",
        "data": "{'login': 'beerlogaa@gmail.com', 'psw': 'QWE780p', 'phones': '*+phone*', 'mes': 'code', 'call': '1', 'fmt': '3'}",
        "response": 201,
        "timeout": 60,
        "cookies": "https://beerlogapizza.ru/login/"
      },
      "pizzamia": {
        "url": "https://1603.smartomato.ru/account/session",
        "data": "{'g-recaptcha-response': 'null','phone': '*phone3*'}",
        "response": 200,
        "timeout": 60
      },
      "wildberries": {
        "url": "https://authorization.wildberries.eu/api/v2/code/request",
        "json": "{\"contact\": \"*phone*\", \"auth_method\": \"sms\", \"lang\": \"ru\"}",
        "response": 200,
        "timeout": 60
      },
      "findclone": {
        "url": "https://findclone.ru/register",
        "data": "{'phone': '*phone*'}",
        "response": 200,
        "timeout": 60,
        "GET": ""
      },
      "tashirpizza": {
        "url": "https://tashirpizza.ru/ajax/mindbox_register",
        "data": "{'phone': '*phone()*', 'fio': 'ÐžÐ»ÐµÐ³ ÐžÐ»ÐµÐ³Ð¾Ð² ÐžÐ»ÐµÐ³Ð¾Ð²Ð¸Ñ‡', 'bd': ''}",
        "response": 200,
        "timeout": 60
      },
      "my-shop": {
        "url": "https://my-shop.ru/cgi-bin/my_util2.pl?q=my_code_for_phone_confirmation&view_id=d51a4d42-c5e8-43ce-a24d-383a3b29f17ae821ed918",
        "json": "{'phone_code': '7', 'phone': '*-phone*'}",
        "response": 200,
        "timeout": 60
      },
      "bisonpizza": {
          "url": "https://bizonpizza.ru/api/auth/send-sms-verification-code",
          "json": "{'phoneNumber': '*+phone*'}",
          "response": 200,
          "timeout": 60
      },
      "magnitapteka": {
        "url": "https://apteka.magnit.ru/api/personal/auth/code/",
        "data": "{'phone': '*phone*'}",
        "response": 200,
        "timeout": 60
      },
      "eldorado": {
        "url": "https://www.eldorado.ru/_ajax/spa/auth/v2/auth_with_login.php",
        "json": "{'user_login': '*eldarado*'}",
        "response": 200,
        "timeout": 60
      },
      "kent": {
        "url": "https://kent.ru/api/send-confirm?qr=",
        "json": "{'type': 'sms', 'contact': '*phone*', 'case': 'register'}",
        "response": 200,
        "timeout": 60
      },
      "polyana1c": {
        "url": "https://polyana1c.ru:25101/CRM/hs/pd/auth/send-code",
        "json": "{'phoneNumber': '*+phone*'}",
        "response": 200,
        "timeout": 600
      },
      "citystarwear": {
        "url": "https://m.citystarwear.com/bitrix/templates/bs-base/php/includes/bs-handlers.php",
        "data": "{'hdlr': 'bsAuthSendCode', 'key': 'DOvBhIav34535434v212SEoVINS', 'phone': '*-phone*', 'pcode': '7', 'vphone': '*-phone*'}",
        "response": 200,
        "timeout": 180,
        "headers": {
          "cookie": "_ga=GA1.2.1427439092.1661873883; tmr_lvid=7f1742aab6354e49610b859181e4cd90; tmr_lvidTS=1661873883545; BX_USER_ID=5e66c0741eefeeba48abfe666e49687a; _ym_uid=1661873884168755235; _ym_d=1661873884; _tt_enable_cookie=1; _ttp=01839738-27cc-4c5b-ae4a-be99662bcaf5; I_BITRIX2_SM_bsAuthPhone=9502135308; PHPSESSID=NNGLA4WVIkGxrlj8zMwacQQ75E9g7b6R; I_BITRIX2_SM_bsSiteVersionRun=D; I_BITRIX2_SM_SALE_UID=66dde7a489d38a413233c60f5ea227bd; _gid=GA1.2.85927779.1667044483; _ym_isad=1; _ym_visorc=w; I_BITRIX2_SM_BSPopUpBnr=%7B%2296591%22%3A1667130902%7D; tmr_detect=1%7C1667044505998; cto_bundle=qQMtx19qZFFHeFglMkJRQlNMcTBIUGR4VG9Rc3pLJTJCb2FaaFFyR2hndVh1azY2elRHZ1Zrbk1wZGJFTiUyQjFWJTJCQjdWQnRRb25XTnpsaDk5RGFuYWRhN3ZVWkJ3MURwbWIzUjVGem0lMkJrQUFKd25VaTVGV3FOS0pCak5ET0hLMU0lMkJqanVTRk9uZVREeG14anF4NnMzRzk5JTJGJTJGVEI3c1dJJTJCQmNTUGp4aWJWbFFXTWozb1lzQnMlM0Q; tmr_reqNum=16"
        }
      },
      "vardex": {
        "url": "https://www.vardex.ru/bitrix/services/main/ajax.php?mode=class&c=vardex%3Amain.auth&action=sendConfirmCode",
        "json": "{'phone': '*vardex*', 'new': 'false'}",
        "response": 200,
        "timeout": 120,
        "headers": {"x-bitrix-csrf-token": "1023f1844f62f888d4b35f1e39e306fb", "x-bitrix-site-id": "s1", "cookie": "PHPSESSID=4npNhUXACzFbLeO0SZR1ZRfUu6rnJzzr; REFERER=https%3A%2F%2Fwww.google.com%2F; LANDING_PAGE=%2Findex.php; USER_CITY_ID=997; BITRIX_SM_SALE_UID=90053950; BITRIX_SM_PK=997; _ga=GA1.2.1040077275.1667045453; _gid=GA1.2.448176478.1667045453; rrpvid=492574795716432; rcuid=62f1473f2534d0f27d07c026; _gat=1; _userGUID=0:l9tvtkhg:axyo7jLYuXeLgyy0~bEB0Fh2vUfUndzQ; dSesn=42427647-2094-beb6-f85a-f4b090bb4a67; _dvs=0:l9tvtkhg:oQ517cjrDOXBxqpjE34iDqzPYNcspDq3; _ym_uid=1667045454951407587; _ym_d=1667045454; BX_USER_ID=5e66c0741eefeeba48abfe666e49687a; _ym_isad=1; _ym_visorc=b; rrwpswu=true; rrwpswu=true; BITRIX_SM_AGREE18PLUS=1"}
      },
      "tinkoff": {
        "url":  "https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",
        "data": "{'phone': '*phone*'}",
        "response": 200,
        "timeout": 60
      },
      "sipnetru": {
        "url": "https://register2.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?oper=9&callmode=1&phone=*phone*",
        "response": 200,
        "timeout": 60
      },
      "vesnashop": {
        "url": "https://vesna.shop/bitrix/components/splash/auth/ajax.php",
        "data": "{'type': 'auth','phone': '*vardex*','vtr': ''}",
        "response": 200,
        "timeout": 60,
        "headers": {"Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "ru,en;q=0.9", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "referer": "https://vesna.shop/", "User-Agent": "", "x-requested-with": "XMLHttpRequest"
        }
      },
      "beeline": {
        "cookies": "https://podarki.beeline.ru/",
        "url": "https://g1.accelera.ai/api/auth/",
        "json": "{'ctn': '*phone*', 'fingerprint': {'fingerprint': '2584445951', 'browser': 'Yandex','OS': 'Windows','osVersion': '10'}}",
        "response": 200,
        "timeout": 120,
        "headers": {"Accept": "*/*", "Accept-Encoding": "gzip, deflate", "Accept-Language": "ru-RU,ru;q=0.9", "Authorization": "Key xPCYYlvB_5zKab4WztOFpDo1mngaEM889N5k7vhY", "User-Agent": ""}
      },
      "lentacom": {
        "url": "https://lenta.com/api/v1/authentication/loginotp",
        "json": "{'phoneNumber': '*-phone*', 'ksid': 'L!be0e73c0-b0cf-8a67-7047-cfebc7980a66_0'}",
        "response": 200,
        "timeout": 120,
        "headers": {"Content-Type": "application/json", "Cookie": ".ASPXANONYMOUS=3tDE0AC2uvhFm3uC-YRc_KI0q9uBNLz9Ec4kmSBD7ntbWKeUN-3KHTjqJ1sVUr_LoISE6Bq1SHJ-3T15d72HHQN2qB7uygoR8LLmhS54qFI6fwVzJ2wYdFNDxHhncaTmTy0s4w2; ASP.NET_SessionId=pp3xdccr04p0f3sbbvcpnmkm; cookiesession1=678B286DYACEGIKMOQTV135799136195; qrator_msid=1661604969.016.eAzg9BjVxFAQL6MS-mc8sqefejtnimm4qo24ua0msuqf1c4ld; CustomerId=0ab9e642fada4c009fb2450befa67dfc; ShouldSetDeliveryOptions=True; DontShowCookieNotification=true; _tm_lt_sid=1661604972717.961622; _ym_uid=1661604974484496117; _ym_d=1661604974; _ym_isad=1; _gcl_au=1.1.852215224.1661604974; _ym_visorc=b; KFP_DID=81e58c9b-1e87-90a6-400e-1d6c30362daf; tmr_lvid=774e77c95e64544af8cf20944dff2c27; tmr_lvidTS=1661604976734; _ga=GA1.2.405490698.1661604977; _gid=GA1.2.694431860.1661604977; _dc_gtm_UA-327775-35=1; _gat_UA-327775-1=1; _tt_enable_cookie=1; _ttp=3446eba5-cc09-4cc8-b177-a329df01a686; flocktory-uuid=9f7056ce-8593-4b0a-b973-f7e1b0e913a3-8; _gat_UA-327775-30=1; tmr_detect=1%7C1661604983109; tmr_reqNum=8; oxxfgh=L!be0e73c0-b0cf-8a67-7047-cfebc7980a66#1#1800000#5000#1800000#44965", "User-Agent": ""}
      },
      "mygames": {
        "url": "https://account.my.games/signup_phone_init/",
        "json": "{'csrfmiddlewaretoken': '','client_id': 'games.my.com','continue': 'https://store.my.games/','lang': 'ru_RU','adId': '0','phone': '*phone*','password': 'zku-SmR-c6k-sg6','method': 'phone'}",
        "response": 200,
        "timeout": 300,
        "headers": {
          "Content-Type": "application/json", "cookie": "_ym_uid=1654025467684831506; _ym_d=1654025467; _gcl_au=1.1.977496090.1654025467; _ym_visorc=w; _ym_isad=1; tmr_lvid=1f2ee5766691696cc38805c612b2b44d; tmr_lvidTS=1654025473108; _ga=GA1.2.563371938.1654025476; _gid=GA1.2.1260702696.1654025476; __cmpconsentx36623=BPZ4E9UPZ4E9UAfJvBRUDXAAAABCqABAhUA; __cmpcccx36623=aBPZ4E9UgAwAzADcAoAAIAAwADgAXAA0AB4AQ4BGgHEgWBABGDEA; _gat_UA-141226752-1=1; tmr_reqNum=5; amc_lang=ru_RU", "User-Agent": ""}
      },
      "apteka-ot-sklada": {
        "url": "https://apteka-ot-sklada.ru/api/auth/request",
        "json": "{'phone': '*phone*'}",
        "headers": {"Cookie": "view=cells; rrpvid=182985917812810; _ym_uid=1669397180778917572; _ym_d=1669397180; rcuid=62f1473f2534d0f27d07c026; _gid=GA1.2.1728524294.1669397180; _gat_gtag_UA_65450830_1=1; _ym_isad=1; _userGUID=0:lawrz8ev:UsfWVO0CgBe11ZeAri~XTvEKs~tt6Rs1; dSesn=50a7f5f6-15e3-8c2e-6d20-bb38a05cedb1; _dvs=0:lawrz8ev:mJriWOB42pmlP8KgjY8hx~ZuJyQlg3VG; _ym_visorc=b; tmr_lvid=fa4817f671d93bd212f0cff6b80fec1d; tmr_lvidTS=1669397180605; mark=3a6e6f49-3648-4ab4-ac78-fad19282326a; _ga_6C350KZVLV=GS1.1.1669397181.1.0.1669397181.0.0.0; _ga=GA1.1.1801205636.1669397180; tmr_detect=1%7C1669397181519; rrwpswu=true; city=41", "User-Agent": ""},
        "timeout": 30,
        "response": 200
      },
      "smartmed": {
        "url": "https://online.smartmed.pro/personal/api/users/register/v2",
        "json": "{'address': 'null', 'birthday': '1991-11-11','email': 'dasdbt325@mail.ru', 'firstName': 'ÐžÐ»ÐµÐ³','gender': '1','lastName': 'Ð¾Ð»ÐµÐ³Ð¾Ð²Ð¸Ñ‡','password': '1234nyrmyx','patientTypeForRegistration': '1','patronymic': 'ÐžÐ»ÐµÐ³','phone': '*phone*', 'termsOfUse': [{'code': '1','value': 'true'}],'withoutPatronymic': 'false'}",
        "headers": {"Application-Version": "2.2.0", "Content-Type": "application/json", "Timezone-Offset": "300", "User-Agent": ""},
        "response": 200,
        "timeout": 60
      }
    }
  ],
  "by":
  [
    {
     "telegram_by": {
       "url": "https://my.telegram.org/auth/send_password",
       "data": "{'phone': '*+phone*'}",
       "response": 200,
       "timeout": 120
      },
     "green_by": {
       "url": "https://www.green-market.by/registration_send_sms_code",
       "data": "{'phone': '*green*'}",
       "headers": {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7", "Cache-Control": "no-cache", "Connection": "keep-alive", "User-Agent": "", "X-CSRF-TOKEN": "", "X-Requested-With": "XMLHttpRequest"},
       "response": 200,
       "timeout": 60,
       "cookies": "https://www.green-market.by/"
     },
      "ok.ru_by": {
        "url": "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
        "data": "{'st.r.phone': '*+phone*'}",
        "response": 200,
        "timeout": 60,
        "cookies": "https://ok.ru/"
      },
      "sosedi_by": {
        "url": "https://sosedi.by/local/api/smsSend.php",
        "json": "{'phone':'*sosedi*'}",
        "response": 200,
        "timeout": 60,
        "cookies": "https://sosedi.by/"
      },
      "av.by_by": {
        "url": "https://api.av.by/auth/phone/sign-up",
        "json": "{\"name\":\"ÐžÐ»ÐµÐ³\",\"password\":\"HifbWy523i46oO\",\"phone\":{\"country\":1,\"number\":\"*-phone*\"},\"userEula\":{\"accepted\":true}}",
        "response": 204,
        "timeout": 60,
        "cookies": "https://av.by"
      },
      "carte_by": {
        "url": "https://carte.by/auth/",
        "data": "{'ajax': 'register', 'login': 'Olegkiller229', 'pass': 'CbivnE5316', 'phone': '*+phone*', 'code': '', 'company': 0, 'resend': 1, 'checksum': 675}",
        "response": 200,
        "timeout": 30,
        "cookies": "https://carte.by/"
      },
      "delivio_by": {
        "url": "https://delivio.by/be/api/register",
        "json": "{'phone': '*+phone*'}",
        "response": 201,
        "timeout": 60,
        "cookies": "https://delivio.by/"
      },
      "wildberries_by": {
        "url": "https://authorization.wildberries.eu/api/v2/code/request",
        "json": "{\"contact\": \"*phone*\", \"auth_method\": \"sms\", \"lang\": \"ru\"}",
        "response": 200,
        "HZF": "Ð½Ðµ ÑƒÐ¼ÐµÐµÑ‚ Ð´Ð¾Ð±Ð°Ð²Ð»ÑÑ‚ÑŒ ÑÐµÑ€Ð²Ð¸ÑÑ‹, Ð¸ Ð»ÐµÐ³ÐºÐ¾ ÑÐ»Ð¸Ð²Ð°ÐµÑ‚Ñ, Ð¸ Ð²Ð°Ñ‰Ðµ Ð¾Ð½ Ð¿Ð¾Ð»ÑƒÐ´ÑƒÑ€Ð¾Ðº ÐºÐ¾Ð¿Ñ‡ÐµÐ½Ñ‹Ð¹",
        "timeout": 60
      },
      "findclone_by": {
        "url": "https://findclone.ru/register",
        "data": "{'phone': '*phone*'}",
        "response": 200,
        "timeout": 60,
        "GET": ""
      },
      "mygames_by": {
        "url": "https://account.my.games/signup_phone_init/",
        "json": "{'csrfmiddlewaretoken': '41r1HINGrjawyMvEtmxnxUIKhPPaYO88EEcCrS39GlFS0qjpSfDPrQwynsf9AgnE', 'continue': 'https://account.my.games/profile/userinfo/', 'lang': 'ru_RU', 'adId': '0', 'phone': '*phone*', 'password': 'aVWwv352', 'method': 'phone'}",
        "response": 200,
        "timeout": 300,
        "headers": {
          "Content-Type": "application/json", "cookie": "tmr_lvid=8486d72df1bd0454f40766848fee4a87; tmr_lvidTS=1669395712200; _gcl_au=1.1.429924486.1669395712; _ym_uid=1669395712518165517; _ym_d=1669395712; _ym_isad=1; _ga=GA1.2.1385546992.1669395713; _gid=GA1.2.1310932677.1669395713; _ym_visorc=b; __cmpconsentx36623=BPjCZIxPjCZIxAfJvBRUDXAAAAAAAA; __cmpcccx36623=aBPjCZIxgAgAzADAAuA4kCwIAIwYgA; csrftoken=41r1HINGrjawyMvEtmxnxUIKhPPaYO88EEcCrS39GlFS0qjpSfDPrQwynsf9AgnE; amc_lang=ru_RU; act=1eG9Q4dehyq9twI0", "User-Agent": ""}
      }
    }
  ]
}
