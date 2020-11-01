from function import *

# ==================================================
# 제어신호 xml 파일이 생성이 되면
# 데이터베이스에 로깅하기 위해 value들을 parsing
# 첫번째 매개변수는 str 타입의 xml 파일 경로
filename = 'control.xml'
tmp_list = parsing_XML_control(filename)
edgeNo = tmp_list[0]
traffic_light = tmp_list[1]
how_many = tmp_list[2]
occasion = tmp_list[3]
print("control.xml 에서 parsing한 값")
print("edgeNo : " + edgeNo)
print("traffic_light : " + traffic_light)
print("how_many : " + how_many)
print("occasion : " + occasion)
# ==================================================
# 데이터베이스에 로깅하기 위한 작업은 추후에 !!!!!!!!!!


# ==================================================
# 첫번째 매개변수는 str 타입의 edgeNo
# 두번째 매개변수는 str 타입의 traffic_light
# salt_value = get_salt_value(edgeNo, traffic_light)
# 반환된 값은 str타입의 salt_value
# 현재는 테스트용으로 놔둠
salt_value = "50384679"
print("salt_value " + salt_value)
# ==================================================
filename = 'control.xml'
# 솔트가 추가된 해쉬값을 리턴하는 함수
# 첫번째 매개변수는 str 타입의 파일이름
# 두번째 매개변수는 str 타입의 솔트값
hash_value = make_hash(filename, salt_value)
# 반환된 값은 str 타입의 솔트가 추가된 hash 값
print("hash_value : " + hash_value)
# ==================================================
filename = 'control.xml'
send_binary = xml_hash_value_make_binary(filename, hash_value)
print("send_binary : ", send_binary)