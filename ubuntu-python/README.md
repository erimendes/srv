Criar certificado
gera_srvcer_cet_srvkiok.sh

MDM_KIOSK_CerSrv

 sudo apt-get update
 sudo apt-get upgrade
 sudo apt-get install apache2
 sudo apt-get install mariadb-server
 sudo apt install python3-pip
 sudo pip3 install mysql-connector-python
 sudo pip3 install flup
 sudo python3 -m pip install flup
 sudo apt install python3-mysqldb
 pip list
 lsb_release -a
 #O comando usado para atualizar o pip, o gerenciador de pacotes do Python, para a versão mais recente
 python.exe -m pip install --upgrade pip
 cd /usr/app/prov/scripts
 sudo python3 db_core.py
 mariadb --version
 python3 --version
   25  ftt@001
 sudo scp radar@130.1.190.247:/etc/apache2/sites-available/* /etc/apache2/sites-available/
 mkdir /usr/app/prov
 cd /usr/app/prov/scripts/
 chmod +x ATENÇÃO_RESTORE_backup_devices.sh
 sudo ./ATENÇÃO_RESTORE_backup_devices.sh
 cat ATENÇÃO_RESTORE_backup_devices.sh
 sudo mysql -u root -psenh@001 <  db_prov.sql
 sudo mysql -u root -psenh@001 <  PROVDB.sql
 sudo mysql -u root -psenh@001 <  db_tsp.sql
 sudo scp sptrans@130.1.190.239:/etc/apache2/sites-available/* /etc/apache2/sites-available/
 sudo scp sptrans@130.1.190.247:/etc/apache2/sites-available/* /etc/apache2/sites-available/
 sudo a2ensite oper.conf
 sudo a2ensite 000-default.conf
 sudo systemctl reload apache2
 sudo systemctl status apache2.service
 cd /etc/apache2
 vi apache2.conf
 sudo systemctl status apache2.service
 sudo systemctl reload apache2
 journalctl -xeu apache2.service
 sudo a2dissite oper.conf
 sudo systemctl reload apache2
 sudo a2dissite 000-default.conf
 sudo systemctl reload apache2
 cd /sites-available/
  116  vi 000-default.conf
  117  history | grep pip

  126  pwd
  127  cd /usr/app/prov/scripts/
  136  nano app.py
  137  nano start.sh
  144  /etc/init.d/apache2 status
  145  systemctl status apache2
  147  nano db_core.py
  cd db/
  155  nano run_tsp.sh
  158  cd /etc/apache2/
  160  cd sites-available/
  162  nano 000-default.conf
  167  cd /usr/app/prov/apk/
  173  a2enmod proxy
  174  sudo a2enmod proxy
  175  sudo a2enmod proxy_http
  176  sudo a2enmod proxy_balancer
  177  sudo a2enmod lbmethod_byrequests
  178  systemctl restart apache2
  179  sudo a2enmod rewrite
  180  systemctl restart apache2
  184  cd scripts/
  186  nano app.py
  188  nano app.py
  189  cd oper/
  193  nano prov_core.py
  194  nano stat.sh
  195  python3 app.py
  197  nano app.py
  198  cd jobs/
  208  cd apk/
  210  nano app-release_kiosk_v
  211  nano app-release_kiosk_v2_test.apk
  222  cd scripts/
  224  nano prov_constants.py
  225  nano db_core.py
  226  python3 db_core.py
  227  nano db_core.py
  231  sudo reboot
  232  uname -r
  237  cd prov/scripts/
  250  supo python3 db_core.py
  253  nano db_core.py
  264  whoami
  265  sudo usermod -aG sudo sptrans
  cd /usr/scripts/
  283  nano db_core.py
  284  sudo python3 db_core.py
  288  nano app.py
  292  cd scripts/oper/site/
  299  nano painel.html

sudo systemctl reload apache2
netstat -napot | grep 80
sudo a2ensite oper.conf
sudo a2ensite 000-default.conf
sudo systemctl reload apache2
cat /var/log/apache2/error.log
sudo a2dissite oper.conf
scp radar@130.1.190.239:/usr/lib/apache2/modules/mod_fastcgi.so /tmp/w/
sudo mv /tmp/w/mod_fastcgi.so /usr/lib/apache2/modules/
sudo /etc/init.d/apache2 stop
sudo /etc/init.d/apache2 start
ldd /usr/lib/apache2/modules/mod_fastcgi.so
sudo chown www-data.www-data -R  /usr/app/prov/
sudo apachectl -M
sudo chown -R sptrans:sptrans /usr/app/prov
sudo chown www-data:www-data -R  /usr/app/prov/log






1. **`sudo systemctl reload apache2`**:
   - Este comando recarrega o serviço Apache2. Ele aplica mudanças na configuração sem reiniciar completamente o serviço. É útil quando você faz alterações nos arquivos de configuração do Apache e deseja aplicá-las imediatamente.

2. **`netstat -napot | grep 80`**:
   - O `netstat` é uma ferramenta de linha de comando que exibe informações sobre conexões de rede, tabelas de roteamento, interfaces de rede e mais. A opção `-napot` inclui informações detalhadas, incluindo endereços e portas. `grep 80` filtra a saída para mostrar apenas linhas relacionadas à porta 80, que é a porta padrão para o tráfego HTTP.

3. **`sudo a2ensite oper.conf`**:
   - Este comando habilita um arquivo de configuração de site específico no Apache2. `a2ensite` significa "Apache2 enable site". Neste caso, ele está habilitando o site configurado em `oper.conf`.

4. **`sudo a2ensite 000-default.conf`**:
   - Similar ao comando anterior, mas está habilitando o arquivo de configuração padrão `000-default.conf`. Este é geralmente o site padrão fornecido com uma instalação do Apache.

5. **`sudo systemctl reload apache2`**:
   - Este comando reaparece para recarregar o serviço Apache2, aplicando as alterações feitas pelos comandos `a2ensite`.

6. **`cat /var/log/apache2/error.log`**:
   - Este comando exibe o conteúdo do arquivo de log de erros do Apache. `cat` é usado para concatenar e exibir o conteúdo do arquivo. O arquivo `/var/log/apache2/error.log` contém registros de erros e eventos relacionados ao Apache.

7. **`sudo a2dissite oper.conf`**:
   - Este comando desabilita um arquivo de configuração de site específico no Apache2. `a2dissite` significa "Apache2 disable site". Neste caso, ele está desabilitando o site configurado em `oper.conf`.
