from scapy.all import sniff, IP
import time

def pack_info_extract():
    p_data = []

    # will mmake Double Buffer

    def handle(pack):
        start = time.time()
        p_feat = {}

        if IP in pack:
            p_feat["IPV4_SRC_ADDR"] = pack[IP].src
            p_feat["IPV4_DST_ADDR"] = pack[IP].dst

        p_data.append(p_feat)
        
        print(p_data)

        end = time.time()
        print(f"\n    Test Case {end-start} time    \n")
    
    sniff(prn=handle)


"""
IPV4_SRC_ADDR - DONE
IPV4_DST_ADDR - DONE
L4_SRC_PORT
L4_DST_PORT
PROTOCOL
L7_PROTO
IN_BYTES - c
OUT_BYTES - c
IN_PKTS - c
OUT_PKTS - c
FLOW_DURATION_MILLISECONDS - c
FLOW_START_MILLISECONDS - c
FLOW_END_MILLISECONDS - c
DURATION_IN - c
DURATION_OUT - c
TCP_FLAGS - c
CLIENT_TCP_FLAGS - c
SERVER_TCP_FLAGS - c
MIN_TTL - c
MAX_TTL - c
LONGEST_FLOW_PKT - c
SHORTEST_FLOW_PKT - c
MIN_IP_PKT_LEN - c
MAX_IP_PKT_LEN - c
SRC_TO_DST_SECOND_BYTES - c
DST_TO_SRC_SECOND_BYTES - c
RETRANSMITTED_IN_BYTES - c
RETRANSMITTED_IN_PKTS - c
RETRANSMITTED_OUT_BYTES - c
RETRANSMITTED_OUT_PKTS - c
SRC_TO_DST_AVG_THROUGHPUT - c
DST_TO_SRC_AVG_THROUGHPUT - c
NUM_PKTS_UP_TO_128_BYTES - c
NUM_PKTS_128_TO_256_BYTES - c
NUM_PKTS_256_TO_512_BYTES - c
NUM_PKTS_512_TO_1024_BYTES - c
NUM_PKTS_1024_TO_1514_BYTES - c
TCP_WIN_MAX_IN - c
TCP_WIN_MAX_OUT - c
ICMP_TYPE
ICMP_IPV4_TYPE
DNS_QUERY_ID
DNS_QUERY_TYPE
DNS_TTL_ANSWER - c
FTP_COMMAND_RET_CODE
SRC_TO_DST_IAT_MIN - c
SRC_TO_DST_IAT_MAX - c
SRC_TO_DST_IAT_AVG - c
SRC_TO_DST_IAT_STDDEV - c
DST_TO_SRC_IAT_MIN - c
DST_TO_SRC_IAT_MAX - c
DST_TO_SRC_IAT_AVG - c
DST_TO_SRC_IAT_STDDEV - c       
"""