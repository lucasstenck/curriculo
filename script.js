// Função para carregar a imagem de perfil
function loadProfileImage() {
    const profileImg = document.getElementById('profile-img');
    
    // Se a imagem não carregar, mostrar um placeholder
    profileImg.onerror = function() {
        this.src = 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUwIiBoZWlnaHQ9IjE1MCIgdmlld0JveD0iMCAwIDE1MCAxNTAiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxyZWN0IHdpZHRoPSIxNTAiIGhlaWdodD0iMTUwIiBmaWxsPSIjMzQ5OGRiIi8+CjxjaXJjbGUgY3g9Ijc1IiBjeT0iNjAiIHI9IjIwIiBmaWxsPSJ3aGl0ZSIvPgo8cGF0aCBkPSJNMzAgMTMwQzMwIDExMCA1MCA5MCA3NSA5MEMxMDAgOTAgMTIwIDExMCAxMjAgMTMwIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K';
    };
}

// Função para adicionar efeitos de scroll suave
function addSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Função para adicionar animações de entrada
function addEntryAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observar elementos para animação
    const elementsToAnimate = document.querySelectorAll('.experience-item, .project-item, .skill-category');
    elementsToAnimate.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}

// Função para adicionar tooltips
function addTooltips() {
    const contactItems = document.querySelectorAll('.contact-item');
    
    contactItems.forEach(item => {
        const text = item.textContent.trim();
        if (text) {
            item.title = text;
        }
    });
}

// Função para adicionar funcionalidade de impressão
function addPrintFunctionality() {
    const printButton = document.createElement('button');
    printButton.innerHTML = '<i class="fas fa-print"></i> Imprimir';
    printButton.className = 'print-btn';
    printButton.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: #3498db;
        color: white;
        border: none;
        padding: 10px 15px;
        border-radius: 5px;
        cursor: pointer;
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        z-index: 1000;
        transition: background 0.3s ease;
    `;
    
    printButton.addEventListener('mouseover', () => {
        printButton.style.background = '#2980b9';
    });
    
    printButton.addEventListener('mouseout', () => {
        printButton.style.background = '#3498db';
    });
    
    printButton.addEventListener('click', () => {
        window.print();
    });
    
    document.body.appendChild(printButton);
}

// Função para adicionar modo escuro (opcional)
function addDarkModeToggle() {
    const darkModeButton = document.createElement('button');
    darkModeButton.innerHTML = '<i class="fas fa-moon"></i>';
    darkModeButton.className = 'dark-mode-btn';
    darkModeButton.style.cssText = `
        position: fixed;
        top: 20px;
        right: 80px;
        background: #2c3e50;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 50%;
        cursor: pointer;
        font-size: 16px;
        z-index: 1000;
        transition: background 0.3s ease;
    `;
    
    let isDarkMode = false;
    
    darkModeButton.addEventListener('click', () => {
        isDarkMode = !isDarkMode;
        document.body.classList.toggle('dark-mode');
        darkModeButton.innerHTML = isDarkMode ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
        darkModeButton.style.background = isDarkMode ? '#f39c12' : '#2c3e50';
    });
    
    document.body.appendChild(darkModeButton);
}

// Função para adicionar estilos de impressão
function addPrintStyles() {
    const style = document.createElement('style');
    style.textContent = `
        @media print {
            .print-btn, .dark-mode-btn {
                display: none !important;
            }
            
            body {
                background: white !important;
            }
            
            .container {
                box-shadow: none !important;
                margin: 0 !important;
            }
            
            .left-column {
                background: #2c3e50 !important;
                color: white !important;
            }
        }
        
        .dark-mode {
            background-color: #1a1a1a !important;
        }
        
        .dark-mode .container {
            background: #2d2d2d !important;
            color: #ffffff !important;
        }
        
        .dark-mode .right-column {
            background: #2d2d2d !important;
            color: #ffffff !important;
        }
        
        .dark-mode .experience-item li {
            color: #cccccc !important;
        }
        
        .dark-mode .project-item {
            background: #3d3d3d !important;
        }
    `;
    document.head.appendChild(style);
}

// Inicializar todas as funcionalidades quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', function() {
    loadProfileImage();
    addSmoothScroll();
    addEntryAnimations();
    addTooltips();
    addPrintFunctionality();
    addDarkModeToggle();
    addPrintStyles();
    
    // Adicionar classe para indicar que o JavaScript está funcionando
    document.body.classList.add('js-enabled');
});

// Função para copiar informações de contato
function copyContactInfo(type) {
    let text = '';
    
    switch(type) {
        case 'email':
            text = 'lucaxstenck@gmail.com';
            break;
        case 'phone':
            text = '(21) 9 9777-1729';
            break;
        case 'portfolio':
            text = 'https://lucasstenck.github.io/portifolio/';
            break;
    }
    
    if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(() => {
            showNotification('Informação copiada!');
        });
    } else {
        // Fallback para navegadores mais antigos
        const textArea = document.createElement('textarea');
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
        showNotification('Informação copiada!');
    }
}

// Função para mostrar notificações
function showNotification(message) {
    const notification = document.createElement('div');
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        background: #27ae60;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        z-index: 1001;
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 2000);
}

// Adicionar estilos para animações de notificação
const notificationStyles = document.createElement('style');
notificationStyles.textContent = `
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-50%) translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }
    }
    
    @keyframes slideOut {
        from {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }
        to {
            opacity: 0;
            transform: translateX(-50%) translateY(-20px);
        }
    }
`;
document.head.appendChild(notificationStyles);
