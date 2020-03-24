# setup the proxy for downloading the packages
export http_proxy="`if [ ! -z "${proxy_host}" ]; then \
                        if [ ! -z "${proxy_port}" ]; then \
                            echo "http://${proxy_host}:${proxy_port}"; \
                        else \
                            echo "http://${proxy_host}"; \
                        fi \
                   fi`"

export https_proxy="`if [ ! -z "${proxy_host}" ]; then \
                         if [ ! -z "${proxy_port}" ]; then \
                             echo "https://${proxy_host}:${proxy_port}"; \
                         else \
                             echo "https://${proxy_host}"; \
                         fi \
                     fi`"
export no_proxy="localhost,127.0.0.0/8,::1"
export HTTP_PROXY="${http_proxy}"
export HTTPS_PROXY="${https_proxy}"
export NO_PROXY="${no_proxy}"
