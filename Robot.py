import telebot
import random

bot = telebot.TeleBot("tokenam")
motivational_quotes = [
    "دنبال یه دلیل برای پرواز بگرد حتی وقتی هزار دلیل برای سقوط داری...",
    "گاهی باید بدترین دردها رو بکشی تا بهترین تغییرها رو تجربه کنی...",
    "زندگی آسون‌تر نمیشه، تو قوی‌تر شو.",
    "هر غروبی طلوعی دارد.",
    "برای چیزهایی که می‌خوای تلاش کن، نه آرزو!",
    "اولش سخته، ولی تهش قشنگه."
]
@bot.message_handler(func=lambda m: m.text == "سلام")
def hi(msg):
    bot.send_message(msg.chat.id, "خوش اومدی خوشتیپ یک جمله انگیزشی میخوای؟ پس کامند جمله انگیزشی رو بزن.")

@bot.message_handler(commands=('command0'))
def start(msg):
    bot.send_message(msg.chat.id, random.choice(motivational_quotes))


bot.infinity_polling()

#ERROR
Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 644, in send
    resp = conn.urlopen(
        method=request.method,
    ...<9 lines>...
        chunked=chunked,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0ADD010>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1110, in infinity_polling
    self.polling(non_stop=True, timeout=timeout, long_polling_timeout=long_polling_timeout,
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 logger_level=logger_level, allowed_updates=allowed_updates, restart_on_change=False,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 *args, **kwargs)
                 ^^^^^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1195, in polling
    logger.info('Starting your bot with username: [@%s]', self.user.username)
                                                          ^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 306, in user
    self._user = self.get_me()
                 ~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1382, in get_me
    apihelper.get_me(self.token)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 204, in get_me
    return _make_request(token, method_url)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 162, in _make_request
    result = _get_req_session().request(
        method, request_url, params=params, files=files,
        timeout=(connect_timeout, read_timeout), proxies=proxy)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 665, in send
    raise ConnectTimeout(e, request=request)
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0ADD010>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))
"
2025-09-01 12:02:08,522 (__init__.py:1115 MainThread) ERROR - TeleBot: "Infinity polling exception: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AE9F90>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))"
2025-09-01 12:02:08,539 (__init__.py:1117 MainThread) ERROR - TeleBot: "Exception traceback:
Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 198, in _new_conn
    sock = connection.create_connection(
        (self._dns_host, self.port),
    ...<2 lines>...
        socket_options=self.socket_options,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    raise err
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
    ~~~~~~~~~~~~^^^^
TimeoutError: timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 488, in _make_request
    raise new_e
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
    ~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 1093, in _validate_conn
    conn.connect()
    ~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 753, in connect
    self.sock = sock = self._new_conn()
                       ~~~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 207, in _new_conn
    raise ConnectTimeoutError(
    ...<2 lines>...
    ) from e
urllib3.exceptions.ConnectTimeoutError: (<urllib3.connection.HTTPSConnection object at 0x0000013BD0AE9F90>, 'Connection to api.telegram.org timed out. (connect timeout=15)')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 644, in send
    resp = conn.urlopen(
        method=request.method,
    ...<9 lines>...
        chunked=chunked,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AE9F90>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1110, in infinity_polling
    self.polling(non_stop=True, timeout=timeout, long_polling_timeout=long_polling_timeout,
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 logger_level=logger_level, allowed_updates=allowed_updates, restart_on_change=False,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 *args, **kwargs)
                 ^^^^^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1195, in polling
    logger.info('Starting your bot with username: [@%s]', self.user.username)
                                                          ^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 306, in user
    self._user = self.get_me()
                 ~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1382, in get_me
    apihelper.get_me(self.token)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 204, in get_me
    return _make_request(token, method_url)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 162, in _make_request
    result = _get_req_session().request(
        method, request_url, params=params, files=files,
        timeout=(connect_timeout, read_timeout), proxies=proxy)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 665, in send
    raise ConnectTimeout(e, request=request)
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AE9F90>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))
"
2025-09-01 12:02:26,625 (__init__.py:1115 MainThread) ERROR - TeleBot: "Infinity polling exception: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEA490>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))"
2025-09-01 12:02:26,635 (__init__.py:1117 MainThread) ERROR - TeleBot: "Exception traceback:
Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 198, in _new_conn
    sock = connection.create_connection(
        (self._dns_host, self.port),
    ...<2 lines>...
        socket_options=self.socket_options,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    raise err
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
    ~~~~~~~~~~~~^^^^
TimeoutError: timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 488, in _make_request
    raise new_e
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
    ~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 1093, in _validate_conn
    conn.connect()
    ~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 753, in connect
    self.sock = sock = self._new_conn()
                       ~~~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 207, in _new_conn
    raise ConnectTimeoutError(
    ...<2 lines>...
    ) from e
urllib3.exceptions.ConnectTimeoutError: (<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEA490>, 'Connection to api.telegram.org timed out. (connect timeout=15)')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 644, in send
    resp = conn.urlopen(
        method=request.method,
    ...<9 lines>...
        chunked=chunked,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEA490>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1110, in infinity_polling
    self.polling(non_stop=True, timeout=timeout, long_polling_timeout=long_polling_timeout,
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 logger_level=logger_level, allowed_updates=allowed_updates, restart_on_change=False,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 *args, **kwargs)
                 ^^^^^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1195, in polling
    logger.info('Starting your bot with username: [@%s]', self.user.username)
                                                          ^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 306, in user
    self._user = self.get_me()
                 ~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1382, in get_me
    apihelper.get_me(self.token)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 204, in get_me
    return _make_request(token, method_url)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 162, in _make_request
    result = _get_req_session().request(
        method, request_url, params=params, files=files,
        timeout=(connect_timeout, read_timeout), proxies=proxy)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 665, in send
    raise ConnectTimeout(e, request=request)
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEA490>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))
"
2025-09-01 12:02:44,710 (__init__.py:1115 MainThread) ERROR - TeleBot: "Infinity polling exception: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEA850>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))"
2025-09-01 12:02:44,735 (__init__.py:1117 MainThread) ERROR - TeleBot: "Exception traceback:
Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 198, in _new_conn
    sock = connection.create_connection(
        (self._dns_host, self.port),
    ...<2 lines>...
        socket_options=self.socket_options,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    raise err
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
    ~~~~~~~~~~~~^^^^
TimeoutError: timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 488, in _make_request
    raise new_e
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
    ~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 1093, in _validate_conn
    conn.connect()
    ~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 753, in connect
    self.sock = sock = self._new_conn()
                       ~~~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 207, in _new_conn
    raise ConnectTimeoutError(
    ...<2 lines>...
    ) from e
urllib3.exceptions.ConnectTimeoutError: (<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEA850>, 'Connection to api.telegram.org timed out. (connect timeout=15)')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 644, in send
    resp = conn.urlopen(
        method=request.method,
    ...<9 lines>...
        chunked=chunked,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEA850>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1110, in infinity_polling
    self.polling(non_stop=True, timeout=timeout, long_polling_timeout=long_polling_timeout,
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 logger_level=logger_level, allowed_updates=allowed_updates, restart_on_change=False,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 *args, **kwargs)
                 ^^^^^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1195, in polling
    logger.info('Starting your bot with username: [@%s]', self.user.username)
                                                          ^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 306, in user
    self._user = self.get_me()
                 ~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1382, in get_me
    apihelper.get_me(self.token)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 204, in get_me
    return _make_request(token, method_url)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 162, in _make_request
    result = _get_req_session().request(
        method, request_url, params=params, files=files,
        timeout=(connect_timeout, read_timeout), proxies=proxy)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 665, in send
    raise ConnectTimeout(e, request=request)
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEA850>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))
"
2025-09-01 12:03:02,794 (__init__.py:1115 MainThread) ERROR - TeleBot: "Infinity polling exception: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEA710>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))"
2025-09-01 12:03:02,833 (__init__.py:1117 MainThread) ERROR - TeleBot: "Exception traceback:
Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 198, in _new_conn
    sock = connection.create_connection(
        (self._dns_host, self.port),
    ...<2 lines>...
        socket_options=self.socket_options,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    raise err
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
    ~~~~~~~~~~~~^^^^
TimeoutError: timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 488, in _make_request
    raise new_e
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
    ~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 1093, in _validate_conn
    conn.connect()
    ~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 753, in connect
    self.sock = sock = self._new_conn()
                       ~~~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 207, in _new_conn
    raise ConnectTimeoutError(
    ...<2 lines>...
    ) from e
urllib3.exceptions.ConnectTimeoutError: (<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEA710>, 'Connection to api.telegram.org timed out. (connect timeout=15)')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 644, in send
    resp = conn.urlopen(
        method=request.method,
    ...<9 lines>...
        chunked=chunked,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEA710>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1110, in infinity_polling
    self.polling(non_stop=True, timeout=timeout, long_polling_timeout=long_polling_timeout,
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 logger_level=logger_level, allowed_updates=allowed_updates, restart_on_change=False,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 *args, **kwargs)
                 ^^^^^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1195, in polling
    logger.info('Starting your bot with username: [@%s]', self.user.username)
                                                          ^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 306, in user
    self._user = self.get_me()
                 ~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1382, in get_me
    apihelper.get_me(self.token)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 204, in get_me
    return _make_request(token, method_url)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 162, in _make_request
    result = _get_req_session().request(
        method, request_url, params=params, files=files,
        timeout=(connect_timeout, read_timeout), proxies=proxy)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 665, in send
    raise ConnectTimeout(e, request=request)
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEA710>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))
"
2025-09-01 12:03:20,967 (__init__.py:1115 MainThread) ERROR - TeleBot: "Infinity polling exception: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEAE90>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))"
2025-09-01 12:03:20,985 (__init__.py:1117 MainThread) ERROR - TeleBot: "Exception traceback:
Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 198, in _new_conn
    sock = connection.create_connection(
        (self._dns_host, self.port),
    ...<2 lines>...
        socket_options=self.socket_options,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    raise err
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
    ~~~~~~~~~~~~^^^^
TimeoutError: timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 488, in _make_request
    raise new_e
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
    ~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 1093, in _validate_conn
    conn.connect()
    ~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 753, in connect
    self.sock = sock = self._new_conn()
                       ~~~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 207, in _new_conn
    raise ConnectTimeoutError(
    ...<2 lines>...
    ) from e
urllib3.exceptions.ConnectTimeoutError: (<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEAE90>, 'Connection to api.telegram.org timed out. (connect timeout=15)')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 644, in send
    resp = conn.urlopen(
        method=request.method,
    ...<9 lines>...
        chunked=chunked,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEAE90>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1110, in infinity_polling
    self.polling(non_stop=True, timeout=timeout, long_polling_timeout=long_polling_timeout,
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 logger_level=logger_level, allowed_updates=allowed_updates, restart_on_change=False,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 *args, **kwargs)
                 ^^^^^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1195, in polling
    logger.info('Starting your bot with username: [@%s]', self.user.username)
                                                          ^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 306, in user
    self._user = self.get_me()
                 ~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1382, in get_me
    apihelper.get_me(self.token)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 204, in get_me
    return _make_request(token, method_url)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 162, in _make_request
    result = _get_req_session().request(
        method, request_url, params=params, files=files,
        timeout=(connect_timeout, read_timeout), proxies=proxy)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 665, in send
    raise ConnectTimeout(e, request=request)
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEAE90>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))
"
2025-09-01 12:03:39,087 (__init__.py:1115 MainThread) ERROR - TeleBot: "Infinity polling exception: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEB250>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))"
2025-09-01 12:03:39,098 (__init__.py:1117 MainThread) ERROR - TeleBot: "Exception traceback:
Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 198, in _new_conn
    sock = connection.create_connection(
        (self._dns_host, self.port),
    ...<2 lines>...
        socket_options=self.socket_options,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    raise err
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
    ~~~~~~~~~~~~^^^^
TimeoutError: timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 488, in _make_request
    raise new_e
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
    ~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 1093, in _validate_conn
    conn.connect()
    ~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 753, in connect
    self.sock = sock = self._new_conn()
                       ~~~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 207, in _new_conn
    raise ConnectTimeoutError(
    ...<2 lines>...
    ) from e
urllib3.exceptions.ConnectTimeoutError: (<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEB250>, 'Connection to api.telegram.org timed out. (connect timeout=15)')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 644, in send
    resp = conn.urlopen(
        method=request.method,
    ...<9 lines>...
        chunked=chunked,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEB250>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1110, in infinity_polling
    self.polling(non_stop=True, timeout=timeout, long_polling_timeout=long_polling_timeout,
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 logger_level=logger_level, allowed_updates=allowed_updates, restart_on_change=False,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 *args, **kwargs)
                 ^^^^^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1195, in polling
    logger.info('Starting your bot with username: [@%s]', self.user.username)
                                                          ^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 306, in user
    self._user = self.get_me()
                 ~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1382, in get_me
    apihelper.get_me(self.token)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 204, in get_me
    return _make_request(token, method_url)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 162, in _make_request
    result = _get_req_session().request(
        method, request_url, params=params, files=files,
        timeout=(connect_timeout, read_timeout), proxies=proxy)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 665, in send
    raise ConnectTimeout(e, request=request)
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEB250>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))
"
2025-09-01 12:03:57,163 (__init__.py:1115 MainThread) ERROR - TeleBot: "Infinity polling exception: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEB610>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))"
2025-09-01 12:03:57,173 (__init__.py:1117 MainThread) ERROR - TeleBot: "Exception traceback:
Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 198, in _new_conn
    sock = connection.create_connection(
        (self._dns_host, self.port),
    ...<2 lines>...
        socket_options=self.socket_options,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    raise err
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
    ~~~~~~~~~~~~^^^^
TimeoutError: timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 488, in _make_request
    raise new_e
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
    ~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 1093, in _validate_conn
    conn.connect()
    ~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 753, in connect
    self.sock = sock = self._new_conn()
                       ~~~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 207, in _new_conn
    raise ConnectTimeoutError(
    ...<2 lines>...
    ) from e
urllib3.exceptions.ConnectTimeoutError: (<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEB610>, 'Connection to api.telegram.org timed out. (connect timeout=15)')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 644, in send
    resp = conn.urlopen(
        method=request.method,
    ...<9 lines>...
        chunked=chunked,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEB610>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1110, in infinity_polling
    self.polling(non_stop=True, timeout=timeout, long_polling_timeout=long_polling_timeout,
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 logger_level=logger_level, allowed_updates=allowed_updates, restart_on_change=False,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 *args, **kwargs)
                 ^^^^^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1195, in polling
    logger.info('Starting your bot with username: [@%s]', self.user.username)
                                                          ^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 306, in user
    self._user = self.get_me()
                 ~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1382, in get_me
    apihelper.get_me(self.token)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 204, in get_me
    return _make_request(token, method_url)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 162, in _make_request
    result = _get_req_session().request(
        method, request_url, params=params, files=files,
        timeout=(connect_timeout, read_timeout), proxies=proxy)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 665, in send
    raise ConnectTimeout(e, request=request)
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEB610>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))
"
2025-09-01 12:04:15,255 (__init__.py:1115 MainThread) ERROR - TeleBot: "Infinity polling exception: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEB9D0>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))"
2025-09-01 12:04:15,265 (__init__.py:1117 MainThread) ERROR - TeleBot: "Exception traceback:
Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 198, in _new_conn
    sock = connection.create_connection(
        (self._dns_host, self.port),
    ...<2 lines>...
        socket_options=self.socket_options,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    raise err
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
    ~~~~~~~~~~~~^^^^
TimeoutError: timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 488, in _make_request
    raise new_e
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
    ~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 1093, in _validate_conn
    conn.connect()
    ~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 753, in connect
    self.sock = sock = self._new_conn()
                       ~~~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 207, in _new_conn
    raise ConnectTimeoutError(
    ...<2 lines>...
    ) from e
urllib3.exceptions.ConnectTimeoutError: (<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEB9D0>, 'Connection to api.telegram.org timed out. (connect timeout=15)')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 644, in send
    resp = conn.urlopen(
        method=request.method,
    ...<9 lines>...
        chunked=chunked,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEB9D0>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1110, in infinity_polling
    self.polling(non_stop=True, timeout=timeout, long_polling_timeout=long_polling_timeout,
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 logger_level=logger_level, allowed_updates=allowed_updates, restart_on_change=False,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 *args, **kwargs)
                 ^^^^^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1195, in polling
    logger.info('Starting your bot with username: [@%s]', self.user.username)
                                                          ^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 306, in user
    self._user = self.get_me()
                 ~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1382, in get_me
    apihelper.get_me(self.token)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 204, in get_me
    return _make_request(token, method_url)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 162, in _make_request
    result = _get_req_session().request(
        method, request_url, params=params, files=files,
        timeout=(connect_timeout, read_timeout), proxies=proxy)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 665, in send
    raise ConnectTimeout(e, request=request)
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEB9D0>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))
"
2025-09-01 12:04:33,291 (__init__.py:1115 MainThread) ERROR - TeleBot: "Infinity polling exception: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEBD90>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))"
2025-09-01 12:04:33,308 (__init__.py:1117 MainThread) ERROR - TeleBot: "Exception traceback:
Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 198, in _new_conn
    sock = connection.create_connection(
        (self._dns_host, self.port),
    ...<2 lines>...
        socket_options=self.socket_options,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    raise err
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
    ~~~~~~~~~~~~^^^^
TimeoutError: timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 488, in _make_request
    raise new_e
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
    ~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 1093, in _validate_conn
    conn.connect()
    ~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 753, in connect
    self.sock = sock = self._new_conn()
                       ~~~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 207, in _new_conn
    raise ConnectTimeoutError(
    ...<2 lines>...
    ) from e
urllib3.exceptions.ConnectTimeoutError: (<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEBD90>, 'Connection to api.telegram.org timed out. (connect timeout=15)')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 644, in send
    resp = conn.urlopen(
        method=request.method,
    ...<9 lines>...
        chunked=chunked,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEBD90>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1110, in infinity_polling
    self.polling(non_stop=True, timeout=timeout, long_polling_timeout=long_polling_timeout,
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 logger_level=logger_level, allowed_updates=allowed_updates, restart_on_change=False,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 *args, **kwargs)
                 ^^^^^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1195, in polling
    logger.info('Starting your bot with username: [@%s]', self.user.username)
                                                          ^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 306, in user
    self._user = self.get_me()
                 ~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1382, in get_me
    apihelper.get_me(self.token)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 204, in get_me
    return _make_request(token, method_url)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 162, in _make_request
    result = _get_req_session().request(
        method, request_url, params=params, files=files,
        timeout=(connect_timeout, read_timeout), proxies=proxy)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 665, in send
    raise ConnectTimeout(e, request=request)
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEBD90>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))
"
2025-09-01 12:04:51,347 (__init__.py:1115 MainThread) ERROR - TeleBot: "Infinity polling exception: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEA5D0>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))"
2025-09-01 12:04:51,364 (__init__.py:1117 MainThread) ERROR - TeleBot: "Exception traceback:
Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 198, in _new_conn
    sock = connection.create_connection(
        (self._dns_host, self.port),
    ...<2 lines>...
        socket_options=self.socket_options,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    raise err
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
    ~~~~~~~~~~~~^^^^
TimeoutError: timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 488, in _make_request
    raise new_e
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
    ~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 1093, in _validate_conn
    conn.connect()
    ~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 753, in connect
    self.sock = sock = self._new_conn()
                       ~~~~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connection.py", line 207, in _new_conn
    raise ConnectTimeoutError(
    ...<2 lines>...
    ) from e
urllib3.exceptions.ConnectTimeoutError: (<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEA5D0>, 'Connection to api.telegram.org timed out. (connect timeout=15)')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 644, in send
    resp = conn.urlopen(
        method=request.method,
    ...<9 lines>...
        chunked=chunked,
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEA5D0>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1110, in infinity_polling
    self.polling(non_stop=True, timeout=timeout, long_polling_timeout=long_polling_timeout,
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 logger_level=logger_level, allowed_updates=allowed_updates, restart_on_change=False,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 *args, **kwargs)
                 ^^^^^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1195, in polling
    logger.info('Starting your bot with username: [@%s]', self.user.username)
                                                          ^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 306, in user
    self._user = self.get_me()
                 ~~~~~~~~~~~^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\__init__.py", line 1382, in get_me
    apihelper.get_me(self.token)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 204, in get_me
    return _make_request(token, method_url)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\telebot\apihelper.py", line 162, in _make_request
    result = _get_req_session().request(
        method, request_url, params=params, files=files,
        timeout=(connect_timeout, read_timeout), proxies=proxy)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\requests\adapters.py", line 665, in send
    raise ConnectTimeout(e, request=request)
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot8462658571:***********************************/getMe (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000013BD0AEA5D0>, 'Connection to api.telegram.org timed out. (connect timeout=15)'))
"

