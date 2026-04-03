document.addEventListener('DOMContentLoaded', () => {
            // 1. Text Split Animation for Hero
            const textToSplit = "Are You Ready?";
            const splitContainer = document.getElementById('splitHeroText');
            if (splitContainer) {
                let splitHTML = ""; 
                let wordStart = true;
                for(let i=0; i<textToSplit.length; i++){ 
                    const char=textToSplit[i]; 
                    if(char===" ") { 
                        splitHTML += "&nbsp;"; wordStart=true; 
                    } else { 
                        if(wordStart){ 
                            splitHTML += "<span class='char-wrap'><i class='char hero-italic' style='transition-delay: "+(0.1+(i*0.05))+"s'>"+char+"</i></span>"; 
                        }else{ 
                            splitHTML += "<span class='char-wrap'><span class='char' style='transition-delay: "+(0.1+(i*0.05))+"s'>"+char+"</span></span>"; 
                        } 
                        wordStart=false; 
                    } 
                }
                splitContainer.innerHTML = splitHTML; 
                setTimeout(() => { document.getElementById('hero').classList.add('animated'); }, 100);
            }

            // 2. Intersection Observer for Fade Up components
            const observerOptions = {
                root: null,
                rootMargin: '0px',
                threshold: 0.15
            };
            
            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if(entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        
                        // If element contains highlights, animate them too
                        const highlights = entry.target.querySelectorAll('.highlight');
                        highlights.forEach(hl => hl.classList.add('animated'));
                        
                        observer.unobserve(entry.target);
                    }
                });
            }, observerOptions);
            
            const fadeElements = document.querySelectorAll('.fade-up, .editor-card, .article-body > *');
            fadeElements.forEach(el => observer.observe(el));
            
            // 3. Scroll Interactions (Navbar, Progress Bar, Parallax)
            const navbar = document.getElementById('navbar');
            const progressBar = document.getElementById('progressBar');
            const heroFilmStrip = document.getElementById('heroFilmStrip');
            const parallaxImgs = document.querySelectorAll('.parallax-img');
            
            window.addEventListener('scroll', () => {
                const scrolled = window.scrollY;
                const winHeight = window.innerHeight;
                const docHeight = document.documentElement.scrollHeight;
                
                // Navbar style
                if (scrolled > 50) {
                    navbar.classList.add('scrolled');
                } else {
                    navbar.classList.remove('scrolled');
                }
                
                // Progress Bar
                const scrollPercent = (scrolled / (docHeight - winHeight)) * 100;
                progressBar.style.width = scrollPercent + '%';
                
                // Simple Parallax for Film Strip
                if(heroFilmStrip && scrolled < winHeight) {
                    heroFilmStrip.style.transform = `translateX(${scrolled * 0.1}px)`;
                }
                
                // Parallax for certain images 
                parallaxImgs.forEach(img => {
                    const rect = img.parentElement.getBoundingClientRect();
                    // If partially in view
                    if(rect.top < winHeight && rect.bottom > 0) {
                        const yOffset = (rect.top - winHeight/2) * 0.1;
                        img.style.transform = `scale(1.1) translateY(${yOffset}px)`;
                    }
                });
                
            }, { passive: true });
            
            // 4. Mobile Menu Toggle
            const menuToggle = document.getElementById('menuToggle');
            const mobileMenu = document.getElementById('mobileMenu');
            const mobileLinks = document.querySelectorAll('.mobile-nav-link');
            
            function toggleMenu() {
                menuToggle.classList.toggle('active');
                mobileMenu.classList.toggle('open');
                if(mobileMenu.classList.contains('open')) {
                    document.body.style.overflow = 'hidden';
                } else {
                    document.body.style.overflow = '';
                }
            }
            
            menuToggle.addEventListener('click', toggleMenu);
            mobileLinks.forEach(link => {
                link.addEventListener('click', toggleMenu);
            });
        });