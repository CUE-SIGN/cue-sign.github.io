# CUE 영화 웹진 — 메인 페이지 + 아티클 상세 페이지 구현 계획

## 배경 및 목표

CUE 독립영화 웹진에 다음 **두 가지 핵심 기능**을 구현합니다:

1. **메인 페이지 (대문)** — `index.html`: 잡지의 첫인상. 모든 카테고리의 아티클을 한눈에 탐색
2. **아티클 상세 페이지** — 개별 `.html` 파일: 카드 클릭 시 새 페이지에서 본문 열람

`loop-landing` 프롬프트 체계(생성자-평가자 피드백 루프)의 **디자인 원칙과 품질 기준**을 적용하여 프리미엄 수준으로 고도화합니다.

---

## 현재 상태 분석

### 이미 구현된 것 ✅

| 항목 | 상태 | 파일 |
|------|------|------|
| 메인 페이지 (대문) | ✅ 기본 구현 | [index.html](file:///c:/Users/USER/Desktop/영화잡지/index.html) |
| 카테고리 페이지 (Ready/Action/Cut) | ✅ 기본 구현 | `ready.html`, `action.html`, `cut.html` |
| 아티클 상세 페이지 (인터뷰) | ✅ 기본 구현 | [action_interview_001.html](file:///c:/Users/USER/Desktop/영화잡지/action_interview_001.html) |
| 아티클 상세 페이지 (에세이) | ✅ 기본 구현 | [cut_008.html](file:///c:/Users/USER/Desktop/영화잡지/cut_008.html) |
| 디자인 시스템 (CSS 변수 토큰) | ✅ 구현됨 | 각 HTML `<style>` 내 |
| Window Card UI 시스템 | ✅ 구현됨 | `.window-card`, `.window-header` 등 |
| 네비게이션 (데스크탑+모바일) | ✅ 구현됨 | 고정 nav + 햄버거 + 오버레이 메뉴 |
| 스크롤 인터랙션 | ✅ 기본 구현 | progress bar, parallax, fade-up |
| 아티클 원문 텍스트 | ✅ 1건 존재 | [interview_001.txt](file:///c:/Users/USER/Desktop/영화잡지/article/interview_001.txt) |

### 주요 문제점 🔴

| 문제 | 설명 |
|------|------|
| **CSS/JS 중복** | 동일한 ~900줄의 CSS + ~100줄의 JS가 모든 HTML 파일에 복사-붙여넣기 |
| **아티클 제목 파싱 오류** | `action_interview_001.html`의 `<title>`과 `<h1>`에 `Short Description:` 텍스트가 깨져서 포함됨 |
| **카드 → 아티클 링크 불일치** | `index.html`에서 `ready_002.html`, `ready_003.html` 등 아직 존재하지 않는 파일로 연결 |
| **아티클 상세 레이아웃** | 일부 상세 페이지(`cut_008.html` 등)에 본문 콘텐츠 없이 껍데기만 존재 |
| **모바일 메뉴 닫힘 태그 누락** | `action_interview_001.html`에서 `.mobile-menu` div가 닫히지 않은 채 본문이 시작됨 |

---

## User Review Required

> [!IMPORTANT]
> **구현 전략 선택이 필요합니다.** 아래 두 가지 옵션 중 선호하는 방향을 알려주세요.

### Option A: 구조 리팩토링 + 고도화 (권장)
- 공통 CSS → `css/global.css`로 분리
- 공통 JS → `js/main.js`로 분리
- 아티클 상세 전용 CSS → `css/article.css`로 분리
- 이후 각 HTML은 `<link>`와 `<script>`로 참조만 하는 구조
- **장점**: 유지보수 용이, 한번 수정으로 전체 반영
- **단점**: 기존 파일 전체 수정 필요

### Option B: 기존 구조 유지하며 고도화
- 현재처럼 각 HTML에 CSS/JS 인라인 유지
- 메인 페이지와 아티클 상세 페이지만 고도화
- **장점**: 빠른 작업, 기존 파일 영향 최소화
- **단점**: 추후 수정 시 모든 파일을 일일이 변경해야 함

---

## Proposed Changes

### 1. 메인 페이지 (대문) — `index.html` 고도화

loop-landing의 `01_generator.md` 원칙을 적용합니다.

#### 1-1. Hero 섹션 강화
- [x] 텍스트 스플릿 애니메이션 (이미 구현됨)
- [ ] 배경 그라디언트 메시를 좀 더 극적으로 (radial → conic/mesh 조합)
- [ ] 필름 스트립 패럴랙스 (이미 구현됨, 미세 조정)
- [ ] CTA 버튼 또는 스크롤 유도 인디케이터 추가 (아래로 스크롤↓ 바운스 애니메이션)

#### 1-2. 카드 인터랙션 고도화
- [ ] Window Card 호버 시 이미지 zoom + 옐로우 틴트 오버레이 (이미 기본 구현, 미세 조정)
- [ ] 카드 순차 등장 시 `transition-delay` 기반의 스태거드 애니메이션 강화
- [ ] CUT 섹션(텍스트 전용 카드)에 호버 시 보더 컬러 변화 + 미묘한 배경 그라디언트 추가

#### 1-3. 메인 페이지 내 카드 → 아티클 링크 정리
- [ ] 존재하지 않는 아티클 파일들의 href를 `#` 또는 실제 파일로 정리
- [ ] 존재하는 아티클: `ready_001.html`, `action_004.html`, `action_005.html`, `action_interview_001.html`, `cut_008.html`, `cut_009.html`

#### 1-4. 뉴스레터/Featured 섹션
- [ ] 이메일 입력 포커스 시 shimmer 효과
- [ ] Featured 카드의 호버 인터랙션 미세 조정

---

### 2. 아티클 상세 페이지 고도화

현재 `action_interview_001.html`을 기준 템플릿으로 삼아 개선합니다.

#### 2-1. 아티클 레이아웃 구조

```
┌─────────────────────────────────────────┐
│  Navigation (고정)                       │
├─────────────────────────────────────────┤
│  Breadcrumb: Home > Action > Interview  │
├─────────────────────────────────────────┤
│  Article Title (h1)                     │
│  Subtitle / Lead (p, italic)            │
│  Meta: category · author · date · read  │
├─────────────────────────────────────────┤
│  Hero Image (16:10)                     │
├───────────────────────┬─────────────────┤
│                       │                 │
│  Article Body (본문)   │  Sidebar        │
│  - h2 소제목           │  - Share        │
│  - p 본문              │  - Featured     │
│  - blockquote 인용     │  - Topics       │
│                       │                 │
├───────────────────────┴─────────────────┤
│  Previous / Next 네비게이션              │
├─────────────────────────────────────────┤
│  Footer                                 │
└─────────────────────────────────────────┘
```

#### 2-2. 타이포그래피 고도화
- [ ] 본문 `font-size: 1.15rem`, `line-height: 1.9` (이미 적용됨, 미세 조정)
- [ ] `blockquote` 스타일을 더 극적으로 — 옐로우 하이라이트 바 + 큰 따옴표 장식
- [ ] 소제목(`h2`) 앞에 장식용 넘버링 또는 대시 추가
- [ ] 드롭캡(첫 글자 크게) 적용 검토

#### 2-3. 아티클 내 인터랙션
- [ ] 본문 요소(p, h2, blockquote)가 스크롤 시 순차적으로 fade-up 등장
- [ ] Hero 이미지에 미묘한 패럴랙스 효과
- [ ] 사이드바 `sticky` 포지셔닝 (이미 구현됨)
- [ ] Share 링크 클릭 시 "링크 복사 완료" 토스트 알림

#### 2-4. Previous/Next 네비게이션
- [ ] 이전/다음 아티클 카드에 화살표 아이콘 + 호버 시 배경 색상 변화
- [ ] 올바른 이전/다음 아티클 URL 연결

#### 2-5. `<title>` 및 `<h1>` 파싱 오류 수정
- [ ] `action_interview_001.html`의 title/h1에서 `Short Description:` 잔여 텍스트 제거

---

### 3. 코드 구조 (Option A 선택 시)

#### [NEW] `css/global.css`
- 디자인 토큰 (`:root` 변수)
- 리셋 스타일
- Typography, Utility, Card System, Navigation, Footer, Responsive
- 약 900줄 → 공통 파일 하나로 통합

#### [NEW] `css/article.css`
- Breadcrumb, Category Hero, Page Layout, Sidebar, Article Body 전용 스타일
- 약 60줄

#### [NEW] `js/main.js`
- IntersectionObserver (fade-up)
- Navbar scroll 핸들러
- Progress bar
- Parallax
- Mobile menu toggle
- 약 80줄

#### [MODIFY] 모든 기존 HTML 파일
- 인라인 `<style>` → `<link rel="stylesheet" href="css/global.css">`
- 인라인 `<script>` → `<script src="js/main.js">`
- 아티클 상세 페이지는 추가로 `css/article.css` 링크

---

### 4. loop-landing 프로세스 적용

`00_loop_master.md`의 SOP를 본 프로젝트에 맞게 적용합니다:

| 단계 | 설명 |
|------|------|
| **Step 1 — Generate** | 메인 페이지 + 아티클 상세 페이지 고도화 코드 작성 |
| **Step 1.5 — Build** | 브라우저에서 열어 렌더링 확인, 콘솔 에러 점검 |
| **Step 2 — Evaluate** | `02_evaluator.md`의 4축 루브릭으로 자체 평가 (시각적 완성도 / 인터랙션 품질 / 코드 품질 / UX 설계) |
| **Step 3 — Revise** | 90점 미달 시 피드백 수용 후 수정, 최대 3사이클 |

---

## Open Questions

> [!IMPORTANT]
> 아래 질문에 답변해주시면 구현을 시작하겠습니다.

1. **구현 전략**: Option A (구조 리팩토링) vs Option B (기존 구조 유지) 중 어떤 것을 선호하시나요?

2. **아티클 콘텐츠**: 현재 `article/interview_001.txt` 외에 추가 아티클 원문이 있나요? (예: cut_008, cut_009 등의 본문 텍스트) 없는 아티클은 플레이스홀더 텍스트로 채울까요?

3. **깨진 링크 처리**: `index.html`에서 아직 존재하지 않는 페이지(`ready_002.html`, `ready_003.html`, `action_006.html`, `cut_010.html`)로의 링크가 있는데, 이 파일들도 생성할까요, 아니면 링크만 정리할까요?

4. **loop-landing 루프 적용**: 실제로 생성→평가 피드백 루프를 돌려가며 고도화를 진행할까요, 아니면 한번에 최선의 결과물을 만들까요?

---

## Verification Plan

### 브라우저 검증
- `index.html`을 브라우저에서 열어 모든 섹션 렌더링 확인
- 아티클 카드 클릭 → 상세 페이지 정상 이동 확인
- 상세 페이지에서 본문 레이아웃, 사이드바, Previous/Next 확인

### 반응형 검증
- 데스크탑 (1440px), 태블릿 (768px), 모바일 (375px) 각각 확인
- 모바일 햄버거 메뉴 동작 확인

### 인터랙션 검증
- 카드 호버 효과 (translate + box-shadow + image zoom)
- Scroll progress bar 동작
- Fade-up 등장 애니메이션
- 네비게이션 scroll 시 배경 변화
