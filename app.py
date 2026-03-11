import streamlit as st
import random

# [데이터 섹션] 1~52번 데이터 (기존과 동일)
kanji_data = [
    {"kanji": "假", "mean": "거짓 가", "examples": [("假令", "가령", "가정해서 말하자면"), ("假熱", "가열", "실제 원인은 차가움인데 열인 것처럼 드러나는 증상")]},
    {"kanji": "嘉", "mean": "아름다울 가", "examples": [("喩嘉言", "유가언", "청나라 때의 한의학자"), ("嘉俳節", "가배절", "추석을 달리 이르는 말")]},
    {"kanji": "家", "mean": "집 가", "examples": [("道家", "도가", "노자와 장자 사상을 따르는 학파"), ("胃家", "위가", "위, 소장, 대장 등 소화기의 통칭")]},
    {"kanji": "歌", "mean": "노래 가", "examples": [("穴性歌", "혈성가", "穴 자리와 그 성질을 외우기 쉽게 노래 형식으로 만든 것"), ("藥性歌", "약성가", "약의 성질과 효능을 외우기 쉽게 노래 형식으로 만든 것")]},
    {"kanji": "街", "mean": "거리 가", "examples": [("氣街", "기가", "穴 자리 중의 한 종류"), ("街談巷說", "가담항설", "사람들 사이에 떠도는 이야기")]},
    {"kanji": "瘕", "mean": "뱃병 가", "examples": [("瘕聚", "가취", "뱃속의 덩어리"), ("血瘕", "혈가", "아랫배에 어혈이 뭉친 증상")]},
    {"kanji": "刻", "mean": "새길 각", "examples": [("百刻", "백각", "하루의 시간을 100등분한 옛 시간 단위"), ("一刻", "일각", "백각이 1,440분이므로 일각은 약 14.4분")]},
    {"kanji": "各", "mean": "각기 각", "examples": [("各家學說", "각가학설", "다양한 의학유파의 학설"), ("各種", "각종", "여러 가지 종류")]},
    {"kanji": "脚", "mean": "다리 각", "examples": [("手脚", "수각", "손과 다리"), ("脚氣", "각기", "다리가 붓는 증상")]},
    {"kanji": "覺", "mean": "깨달을 각", "examples": [("感覺", "감각", "바깥의 자극을 알아차림"), ("覺醒", "각성", "정신을 차림 혹은 깨달아 앎")]},
    {"kanji": "角", "mean": "뿔 각", "examples": [("臭角", "취각", "냄새 맡는 감각. 즉 후각의 다른 말"), ("角弓反張", "각궁반장", "활처럼 몸이 뒤로 젖혀지는 증상")]},
    {"kanji": "閣", "mean": "누각 각", "examples": [("樓閣", "누각", "사방을 바라볼 수 있게 높이 지은 건축물"), ("改閣", "개각", "정부의 내각을 개편함")]},
    {"kanji": "刊", "mean": "책 펴낼 간", "examples": [("刊行", "간행", "인쇄물을 출판함"), ("刊刻", "간각", "글씨를 새김")]},
    {"kanji": "幹", "mean": "줄기 간", "examples": [("幹線", "간선", "주요 구간 사이를 연결하는 선"), ("根幹", "근간", "사물의 근본이나 가장 중심이 되는 부위")]},
    {"kanji": "癎", "mean": "간질 간", "examples": [("癲癎", "전간", "의식을 잃으며 경련성 발작을 하는 질환"), ("癎風", "간풍", "전간(즉 간질)의 일종")]},
    {"kanji": "簡", "mean": "대쪽 간", "examples": [("吳簡", "오간", "송나라 때의 한의학자"), ("簡單", "간단", "간략하고 단순함")]},
    {"kanji": "肝", "mean": "간장 간", "examples": [("肝主疏泄", "간주소설", "간은 소통하고 발설하는 기능을 주관함"), ("肝藏血", "간장혈", "간은 피를 저장함")]},
    {"kanji": "間", "mean": "사이 간", "examples": [("腎間動氣", "신간동기", "두 신장 사이에서 움직이는 기운"), ("劉河間", "유하간", "금원사대가 중 한 사람")]},
    {"kanji": "渴", "mean": "목마를 갈", "examples": [("煩渴", "번갈", "가슴속이 답답하고 목이 마른 증상"), ("消渴", "소갈", "갈증이 나서 물을 많이 먹는 증상")]},
    {"kanji": "竭", "mean": "다할 갈", "examples": [("枯竭", "고갈", "말라서 없어짐"), ("精氣竭", "정기갈", "정기가 다 없어짐")]},
    {"kanji": "葛", "mean": "칡 갈", "examples": [("葛根", "갈근", "한약재 중의 한 종류"), ("葛藤", "갈등", "서로 상치되는 견해/처지 등으로 생기는 충돌")]},
    {"kanji": "坎", "mean": "구덩이 감", "examples": [("坎卦", "감괘", "주역의 팔괘 중의 하나"), ("坎方", "감방", "팔괘 배치도에서 감괘가 위치한 방향")]},
    {"kanji": "感", "mean": "느낄 감", "examples": [("外感", "외감", "외부 환경에 의해 질병이 발생함"), ("상감", "상감", "서로 영향을 주고받음")]},
    {"kanji": "減", "mean": "덜 감", "examples": [("加減", "가감", "더함과 덜어냄"), ("減退", "감퇴", "줄어듦")]},
    {"kanji": "甘", "mean": "달 감", "examples": [("辛酸鹹苦甘", "신산함고감", "맵고 시고 짜고 쓰고 단 맛"), ("甘草", "감초", "한약재의 한 종류")]},
    {"kanji": "監", "mean": "볼 감", "examples": [("卑監", "비감", "운기학에서 土의 기운이 부족한 해"), ("監査", "감사", "보고 검사함")]},
    {"kanji": "鑑", "mean": "거울 감", "examples": [("東醫寶鑑", "동의보감", "조선 시대 허준이 저술한 한의학서"), ("醫宗金鑑", "의종금감", "청나라 때 오겸이 지은 한의학서")]},
    {"kanji": "甲", "mean": "첫째 천간 갑", "examples": [("甲子", "갑자", "중국의 육십년 주기의 첫 번째 해"), ("爪甲", "조갑", "손톱과 발톱을 통틀어 이르는 말")]},
    {"kanji": "剛", "mean": "굳셀 강", "examples": [("剛健", "강건", "마음이 곧고 뜻이 굳셈"), ("剛柔", "강유", "굳셈과 부드러움")]},
    {"kanji": "康", "mean": "평안할 강", "examples": [("健康", "건강", "병이 없이 좋은 기능을 가진 상태"), ("康命吉", "강명길", "조선 시대 한의학자")]},
    {"kanji": "强", "mean": "강할 강", "examples": [("虛實强弱", "허실강약", "허와 실의 강함과 약함"), ("項强", "항강", "목 뒤가 뻣뻣한 증상")]},
    {"kanji": "江", "mean": "강 강", "examples": [("江하", "강하", "강과 하천"), ("江上", "강상", "강의 위")]},
    {"kanji": "綱", "mean": "벼리 강", "examples": [("綱領", "강령", "어떤 일의 근본 원칙"), ("八綱", "팔강", "질병을 감별하는 여덟 가지 원칙")]},
    {"kanji": "腔", "mean": "속이 빌 강", "examples": [("胸腹腔", "흉복강", "가슴과 배 내부의 빈 공간"), ("體腔", "체강", "피부 안쪽 면과 장기 사이의 빈 공간")]},
    {"kanji": "薑", "mean": "생강 강", "examples": [("生薑", "생강", "한약재의 한 종류"), ("乾薑", "건강", "생강을 말린 것")]},
    {"kanji": "講", "mean": "익힐 강", "examples": [("講讀", "강독", "책을 읽고 뜻을 해설함"), ("吳醫匯講", "오의회강", "청나라 때 당대열이 쓴 한의학서")]},
    {"kanji": "降", "mean": "내릴 강", "examples": [("肅降", "숙강", "기를 맑혀 아래로 내려 보내는 작용"), ("降伏", "항복", "적에게 굴복")]},
    {"kanji": "介", "mean": "끼일 개", "examples": [("張介賓", "장개빈", "명나라 때의 한의학자"), ("媒介", "매개", "중간에서 서로의 관계를 맺어 주는 일")]},
    {"kanji": "改", "mean": "고칠 개", "examples": [("醫林改錯", "의림개착", "청나라 때 왕청임이 쓴 한의학서"), ("改善", "개선", "잘못을 고쳐 좋게 함")]},
    {"kanji": "槪", "mean": "대개 개", "examples": [("槪念", "개념", "개별 현상에서 뽑아낸 공통점에 대한 종합적 생각"), ("大槪", "대개", "대부분")]},
    {"kanji": "疥", "mean": "옴 개", "examples": [("乾疥", "건개", "가렵고 짓무르기도 하는 피부 증상(옴)"), ("疥癬", "개선", "건개와 같은 말")]},
    {"kanji": "皆", "mean": "모두 개", "examples": [("皆屬於肝", "개속어간", "모두 간에 속함"), ("百病皆生於氣", "백병개생어기", "온갖 병이 모두 氣에서 생겨남")]},
    {"kanji": "蓋", "mean": "덮을 개", "examples": [("華蓋", "화개", "穴 자리 중의 한 종류"), ("膝蓋骨", "슬개골", "무릎 앞 한가운데의 오목한 뼈")]},
    {"kanji": "開", "mean": "열 개", "examples": [("開闔樞", "개합추", "염과 닫음과 조절함"), ("開竅", "개규", "구멍이 열림")]},
    {"kanji": "客", "mean": "손님 객", "examples": [("邪客", "사객", "사기가 침범함"), ("客氣", "객기", "정상적 기운을 침범한 기운")]},
    {"kanji": "居", "mean": "살 거", "examples": [("起居有常", "기거유상", "일상생활이 일정함"), ("居處", "거처", "사는 곳")]},
    {"kanji": "擧", "mean": "들 거", "examples": [("擧動", "거동", "나서서 움직임"), ("擧重", "거중", "무거운 것을 듦")]},
    {"kanji": "乾", "mean": "하늘 건", "examples": [("乾坤", "건곤", "하늘과 땅"), ("乾咳", "건해", "마른기침")]},
    {"kanji": "健", "mean": "튼튼할 건", "examples": [("健脾", "건비", "비의 기능을 튼튼하게 함"), ("健忘", "건망", "기억을 잘 잊어버리는 증상")]},
    {"kanji": "建", "mean": "세울 건", "examples": [("建議", "건의", "의견을 말함"), ("溫胃建中", "온위건중", "위를 따뜻하게 하고 소화기를 바로 세움")]},
    {"kanji": "檢", "mean": "검사할 검", "examples": [("檢査", "검사", "사실을 살펴봄"), ("檢閱", "검열", "검사하여 살펴봄")]},
    {"kanji": "怯", "mean": "무서워할 겁", "examples": [("食怯", "식겁", "겁을 먹음"), ("勇怯", "용겁", "용기와 겁")]}
]

def init_session():
    if 'score' not in st.session_state:
        st.session_state.score = 0
        st.session_state.current_idx = 0
        st.session_state.wrong_list = []
        st.session_state.quiz_list = random.sample(kanji_data, 30)
        st.session_state.answered = False
        st.session_state.is_correct = False
        st.session_state.target_ex = None
        st.session_state.q_type = None

def main():
    st.set_page_config(page_title="한의학 퀴즈", layout="centered")
    init_session()
    
    st.title("📱 한의학 필수 한자 퀴즈")
    st.markdown("---")
    
    if st.session_state.current_idx < 30:
        target_kanji = st.session_state.quiz_list[st.session_state.current_idx]
        
        if not st.session_state.answered and st.session_state.target_ex is None:
            st.session_state.target_ex = random.choice(target_kanji['examples'])
            st.session_state.q_type = random.randint(1, 4)

        st.subheader(f"문제 {st.session_state.current_idx + 1} / 30")
        
        q_text = ""
        correct_ans = ""
        info_header = ""

        # 질문 구성 및 출처 표시 로직
        if st.session_state.q_type == 1:
            q_text = f"한자 '{target_kanji['kanji']}'의 뜻과 음은?"
            correct_ans = target_kanji['mean']
            info_header = f"📍 한자 문제"
        elif st.session_state.q_type == 2:
            q_text = f"용어 '{st.session_state.target_ex[0]}'의 의미는?"
            correct_ans = st.session_state.target_ex[2]
            info_header = f"📍 용어 문제 (출처 한자: {target_kanji['kanji']} - {target_kanji['mean']})"
        elif st.session_state.q_type == 3:
            q_text = f"한자 '{target_kanji['kanji']}'의 뜻과 음을 직접 쓰세요."
            correct_ans = target_kanji['mean']
            info_header = f"📍 주관식 한자"
        else:
            q_text = f"용어 '{st.session_state.target_ex[0]}'의 한글 음은?"
            correct_ans = st.session_state.target_ex[1]
            info_header = f"📍 주관식 용어 (출처 한자: {target_kanji['kanji']} - {target_kanji['mean']})"

        st.info(info_header)
        st.write(f"### {q_text}")

        if not st.session_state.answered:
            if st.session_state.q_type <= 2: # 객관식
                if st.session_state.q_type == 1:
                    pool = [d['mean'] for d in kanji_data if d['mean'] != correct_ans]
                else:
                    pool = [random.choice(d['examples'])[2] for d in kanji_data if d['kanji'] != target_kanji['kanji']]
                
                options = random.sample(pool, 3) + [correct_ans]
                random.shuffle(options)
                
                for opt in options:
                    if st.button(opt, key=opt, use_container_width=True):
                        check_result(opt, correct_ans, q_text, info_header)
            else: # 주관식
                user_input = st.text_input("정답 입력 후 엔터를 치거나 아래 버튼을 누르세요.", key=f"input_{st.session_state.current_idx}")
                if st.button("제출", type="primary", use_container_width=True):
                    check_result(user_input, correct_ans, q_text, info_header)
        else:
            # 정답/오답 피드백
            if st.session_state.is_correct:
                st.success(f"✨ 정답입니다! (정답: {correct_ans})")
            else:
                st.error(f"❌ 틀렸습니다. 정답: {correct_ans}")
            
            # 용례일 경우 상세 설명 추가 표시
            if st.session_state.q_type in [2, 4]:
                st.write(f"📖 **'{st.session_state.target_ex[0]}'의 뜻:** {st.session_state.target_ex[2]}")
            
            if st.button("다음 문제로 ➡️", type="secondary", use_container_width=True):
                st.session_state.current_idx += 1
                st.session_state.answered = False
                st.session_state.target_ex = None
                st.rerun()
    else:
        st.balloons()
        st.success(f"🏁 최종 점수: {st.session_state.score} / 30")
        
        if st.session_state.wrong_list:
            st.divider()
            st.subheader("📝 오답 노트")
            for w in st.session_state.wrong_list:
                with st.expander(f"Q: {w['q']}"):
                    st.write(f"**{w['header']}**")
                    st.write(f"**나의 오답:** {w['user']}")
                    st.write(f"**진짜 정답:** {w['ans']}")
        
        if st.button("🔄 처음부터 다시하기", use_container_width=True):
            st.session_state.clear()
            st.rerun()

def check_result(user_val, correct_val, q_text, header_text):
    u = user_val.strip().replace(" ", "")
    c = correct_val.strip().replace(" ", "")
    st.session_state.answered = True
    if u == c:
        st.session_state.score += 1
        st.session_state.is_correct = True
    else:
        st.session_state.is_correct = False
        st.session_state.wrong_list.append({
            "header": header_text,
            "q": q_text, 
            "ans": correct_val,
            "user": user_val if user_val else "(미입력)"
        })
    st.rerun()

if __name__ == "__main__":
    main()
