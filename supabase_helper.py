from supabase import create_client, Client

# Supabase URL과 키 설정
supabase_url = "https://ioursknulljozaqqcxvg.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlvdXJza251bGxqb3phcXFjeHZnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjcxNjcxNDcsImV4cCI6MjA0Mjc0MzE0N30.yRZ3Rv5VCEru0WPDvnttW3zKQZ24WqUdh5GRJa548ac"

# Supabase 클라이언트 생성 함수
def create_supabase_client() -> Client:
    """Supabase 클라이언트를 생성하여 반환"""
    return create_client(supabase_url, supabase_key)

# 데이터 조회 함수
def get_calendar_data(supabase_client: Client):
    """Supabase에서 일정을 조회"""
    response = supabase_client.table('minsik_calender').select('*').execute()
    return response.data

# 일정 추가 함수
def add_event_to_supabase(title, date, value, supabase_client: Client):
    """Supabase에 새로운 일정을 추가"""
    data = {"schedule_title": title, "schedule_day": date, "schedule_value": value}
    supabase_client.table('minsik_calender').insert(data).execute()

    
    print("일정이 성공적으로 등록되었습니다.")

    # 특정 날짜에 해당하는 일정 조회 함수
def get_calendar_data_by_date(supabase_client: Client, date: str):
    """선택된 날짜에 해당하는 일정을 조회"""
    response = supabase_client.table('minsik_calender').select('*').eq('schedule_day', date).execute()
    
    return response.data

# 사용자 인증 함수
def verify_login(username, password, supabase_client):
    """Supabase에서 사용자 이름과 비밀번호를 확인하는 함수"""
    try:
        response = supabase_client.table('global_setting').select('*').eq('user_name', username).execute()
        if response.data:  # 데이터가 있을 경우
            user_data = response.data[0]
            return user_data.get('password') == password  # 비밀번호 일치 여부 확인
        else:
            print("사용자 이름을 찾을 수 없습니다.")
            return False
    except Exception as e:
        print(f"로그인 중 오류 발생: {e}")
        return False


