PABNA PHOTO FRAME GENERATOR — GITHUB PAGES

কীভাবে GitHub Pages-এ প্রকাশ করবেন:
1. এই প্রজেক্টের সব ফাইল GitHub repository-র root-এ upload/push করুন (index.html root-এ থাকবে)।
2. Repository > Settings > Pages > Build and deployment > Source থেকে “GitHub Actions” নির্বাচন করুন।
3. Actions tab-এ “Deploy Photo Frame Website to GitHub Pages” workflow সফল হওয়া পর্যন্ত অপেক্ষা করুন।
4. Settings > Pages-এ দেখানো URL ভিজিট করুন। ইউজারদের .bat চালাতে হবে না।

নতুন ফ্রেম যোগ করার নিয়ম:
1. নিজের ফ্রেম PNG/SVG/JPG/JPEG/WebP হিসেবে frames/ ফোল্ডারে রাখুন।
2. ফাইলটি GitHub-এ commit/push করুন।
3. GitHub Actions স্বয়ংক্রিয়ভাবে frames.json তৈরি করে ওয়েবসাইট redeploy করবে। নতুন ফ্রেম সাইটে দেখা যাবে। HTML edit করার দরকার নেই।

গুরুত্বপূর্ণ:
- GitHub Pages হলো static hosting। ব্রাউজার নিজে থেকে frames/ ফোল্ডারের তালিকা পড়তে পারে না। তাই GitHub Actions deploy-এর সময় frames.json তৈরি করে।
- .bat শুধু নিজের Windows কম্পিউটারে local testing-এর জন্য। পাবলিক ওয়েবসাইট ব্যবহার করতে লাগে না।
- PNG frame-এর ছবির জায়গাটি transparent রাখুন, যাতে ইউজারের ছবি নিচে দেখা যায়।
- ফ্রেমের নাম ফাইলের নাম থেকে তৈরি হবে; যেমন science_fest.png -> Science Fest.
- Frames-এর নাম custom করতে চাইলে frames.json তৈরি হওয়ার পর workflow-এর manifest generator-এ mapping যোগ করতে হবে, অথবা filename-এ নাম দিন।
