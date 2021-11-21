# MVP по раздаче монет в тестовой сети Ropsten
## О проекте
Стек проекта: Python 3.8/Django, Postgres, Gunicorn, Web3Py, Bootstrap.

Для фунционирования проекта вам потребуется запустить на бекенде geth rpc-api (127.0.0.1:8545).

Как установить geth описано [тут](https://geth.ethereum.org/docs/install-and-build/installing-geth)

Запустить geth в режиме синхронизации можно командой:

```shell
geth --http --mine --miner.etherbase <address> --ropsten --syncmode fast --snapshot=false --http.api personal,eth,net,web3 --txlookuplimit=0 --cache 1024 --unlock <address> --password <pass_file_root> --keystore <key_store_root>
```
В случае выполнения майнига требуется использовать ключи --mine и --miner.etherbase, где address - адрес получателя намайненных монет.

Ключи --unlock и --password (путь до файла) необходимы для разблокировки аккаунта (используется для текущей работы).

Ключ --keystore необходим для установки пути к хранилищю ключей.

Установка Python и зависимостей можно произвести по инструкции [отсюда](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-ru).
