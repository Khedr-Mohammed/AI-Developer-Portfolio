from flask import Flask, render_template

app = Flask(__name__)

# قائمة المشاريع الهيكلية الخاصة بك (تمرير ديناميكي عبر Jinja)
PROJECTS = [
    {
        "title": "Medical Image Compression",
        "description": "تطوير مشروع أكاديمي يستههدف ضغط صور الأشعة السينية (Chest X-Ray) باستخدام شبكات التعلم العميق وتحديداً Convolutional Autoencoders.",
        "tech_stack": ["Python", "PyTorch", "TensorFlow", "Deep Learning"],
        "github_url": "https://github.com/YOUR-USERNAME/medical-image-compression",
        "image": "images/AutoEncoder.jpg"
    },
    {
        "title": "Tkinter-Calculator",
        "description": "تطبيق آلة حاسبة تفاعلي لسطح المكتب مصمم بلغة بايثون ومكتبة Tkinter مع هيكلية برمجية منظمة واجهة مستخدم نظيفة وسلسة.",
        "tech_stack": ["Python", "Tkinter", "OOP"],
        "github_url": "https://github.com/Khedr-Mohammed/Tkinter_calculater",
        "image": "images/Tkinter Calculator.jpg"
    },
    {
        "title": "AI Developer Portfolio",
        "description": "موقع بورتفوليو شخصي تفاعلي ومتجاوب مبني باستخدام إطار العمل Flask و HTML5/CSS3 لعرض الخلفية الأكاديمية والمشاريع البرمجية.",
        "tech_stack": ["Python", "Flask", "HTML/CSS"],
        "github_url": "https://github.com/YOUR-USERNAME/ai-developer-portfolio",
        "image": "images/AI Developer Protfolio ex.jpg"
    },
    {
        "title": "Password Generator",
        "description": "أداة أمنية برمجية لتوليد كلمات مرور قوية وعشوائية وآمنة بشكل فوري وفق خيارات مخصصة لتأمين الحسابات.",
        "tech_stack": ["Python", "Security", "Random"],
        "github_url": "https://github.com/Khedr-Mohammed/Password-Generator",
        "image": "images/password generator.jpg"
    },
    {
        "title": "Number Guessing Game",
        "description": "لعبة تفاعلية ممتعة لتخمين الأرقام مصممة بلغة بايثون مع خوارزميات تحقق ذكية ومنطق برميلي متسلسل.",
        "tech_stack": ["Python", "Logic", "CLI"],
        "github_url": "https://github.com/Khedr-Mohammed/Number-Guessing-Game",
        "image": "images/Number Guessing Game.jpg"
    },
    {
        "title": "Stock-Tracker",
        "description": "نظام تتبع وتحليل أسعار الأسهم والبيانات المالية الفورية باستخدام واجهات برمجة التطبيقات (APIs) وعرض النتائج بشكل منسق.",
        "tech_stack": ["Python", "APIs", "Finance"],
        "github_url": "https://github.com/Khedr-Mohammed/Stock-Tracker-Using-Python-master",
        "image": "images/stock.jpg"
    },
    {
        "title": "yt_dlp Gui Download From Youtube",
        "description": "تطبيق واجهة مستخدم رسومية (GUI) مدعوم بمكتبة yt_dlp لتحميل الفيديوهات وملفات الصوت من يوتيوب بسهولة وكفاءة عالية.",
        "tech_stack": ["Python", "yt_dlp", "Tkinter"],
        "github_url": "https://github.com/Khedr-Mohammed/ytdlp-gui-master",
        "image": "images/youtube.jpg"
    },
    {
        "title": "Sales Data Analysis",
        "description": "لوحة تحكم تحليلية متكاملة لمعالجة مجموعات البيانات الضخمة واستخراج رؤى إحصائية باستخدام مكتبات Pandas و Seaborn.",
        "tech_stack": ["Python", "Pandas", "Seaborn"],
        "github_url": "https://github.com/Khedr-Mohammed/sales-analysis",
        "image": "images/sales.jpg"
    },
    {
        "title": "Audio Extractor",
        "description": "أداة برمجية فعالة لاستخراج ومعالجة الملفات الصوتية وفصل الطبقات والترددات النقية بدقة عالية وبأداء سريع وسلس.",
        "tech_stack": ["Python", "FFmpeg", "Audio Processing"],
        "github_url": "https://github.com/Khedr-Mohammed/Audio-Extractor-master",
        "image": "images/Audio.jpg"
    },
    {
        "title": "Text To Speech",
        "description": "نموذج ذكاء اصطناعي متقدم لتحويل النصوص المكتوبة إلى كلام منطوق بشري طبيعي باستخدام تقنيات التعلم العميقة ومعالجة الإشارات.",
        "tech_stack": ["Python", "PyTorch", "Deep Learning"],
        "github_url": "https://github.com/Khedr-Mohammed/text-to-speech-master",
        "image": "images/text to speech.jpg"
    },
    {
        "title": "titanic-survival-analysis",
        "description": "نموذج تحليل بيانات وتنبؤ تعتمد خوارزمياته على التعلم الآلي لدراسة بيانات ركاب سفينة التايتانيك والتنبؤ بمعدلات النجاة بدقة.",
        "tech_stack": ["Python", "Scikit-Learn", "Machine Learning"],
        "github_url": "https://github.com/Khedr-Mohammed/titanic-survival-analysis",
        "image": "images/titanic survival analyisis.jpg"
    },
    {
        "title": "Web-Scraping-Data-Parsing",
        "description": "أداة ذكية لاستخراج وتحليل البيانات من صفحات الويب، تقوم بجمع البيانات غير المنظمة وتصفيتها وهيكلتها بدقة داخل جداول منظمة.",
        "tech_stack": ["Python", "BeautifulSoup", "Requests"],
        "github_url": "https://github.com/YOUR-USERNAME/web-scraping-data-parsing",
        "image": "images/web.jpg"
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=PROJECTS)

if __name__ == '__main__':
    app.run(debug=True)