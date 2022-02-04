import subprocess


def init_socat(host_port, client_port):
    """ Иницируем канал на 2 эмулируемых девайса для обмена
    информацией между ними """
    cmd = ['/usr/bin/socat', '-d', '-d', 'PTY,link=%s,raw,echo=0' %
           host_port, 'PTY,link=%s,raw,echo=0' % client_port]
    socat_proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
    return socat_proc
