/* ==========================================================================
   ZHEJIANG MAVEN INDUSTRIAL TECHNOLOGY CO., LTD.
   Vanilla JavaScript for B2B Interactive Website
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initMobileNav();
  initHeaderScroll();
  initCategoryFilters();
  initModal();
  initFormHandler();
  setActiveNavLink();
});

/* --------------------------------------------------------------------------
   1. MOBILE NAVIGATION TOGGLE
   -------------------------------------------------------------------------- */
function initMobileNav() {
  const toggleBtn = document.querySelector('.mobile-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (toggleBtn && navLinks) {
    const closeMenu = () => {
      navLinks.classList.remove('active');
      toggleBtn.setAttribute('aria-expanded', 'false');
      toggleBtn.innerHTML = '&#9776;';
      document.body.style.overflow = '';
    };

    toggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      navLinks.classList.toggle('active');
      const isExpanded = navLinks.classList.contains('active');
      toggleBtn.setAttribute('aria-expanded', isExpanded);
      toggleBtn.innerHTML = isExpanded ? '&#10005;' : '&#9776;';
      document.body.style.overflow = isExpanded ? 'hidden' : '';
    });

    // Close menu when clicking any nav link
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        closeMenu();
      });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
      if (!toggleBtn.contains(e.target) && !navLinks.contains(e.target)) {
        closeMenu();
      }
    });
  }
}

/* --------------------------------------------------------------------------
   2. STICKY HEADER SHADOW ON SCROLL
   -------------------------------------------------------------------------- */
function initHeaderScroll() {
  const header = document.querySelector('.site-header');
  if (header) {
    const handleScroll = () => {
      if (window.scrollY > 10) {
        header.style.boxShadow = '0 4px 20px rgba(15, 56, 44, 0.12)';
        header.style.borderBottomColor = 'transparent';
      } else {
        header.style.boxShadow = 'none';
        header.style.borderBottomColor = 'var(--color-border-light)';
      }
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();
  }
}

/* --------------------------------------------------------------------------
   3. SET ACTIVE NAV LINK BASED ON CURRENT PAGE
   -------------------------------------------------------------------------- */
function setActiveNavLink() {
  const path = window.location.pathname;
  const page = path.split('/').pop() || 'index.html';
  const links = document.querySelectorAll('.nav-link');

  links.forEach(link => {
    const href = link.getAttribute('href');
    if (href === page || (page === '' && href === 'index.html')) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
}

/* --------------------------------------------------------------------------
   4. PRODUCT CATEGORY FILTERING (PRODUCTS PAGE)
   -------------------------------------------------------------------------- */
function initCategoryFilters() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const productCards = document.querySelectorAll('.product-card-item');

  if (filterBtns.length > 0 && productCards.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        // Remove active class from all buttons
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const category = btn.getAttribute('data-filter');

        productCards.forEach(card => {
          if (category === 'all' || card.getAttribute('data-category') === category) {
            card.style.display = 'flex';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }
}

/* --------------------------------------------------------------------------
   5. REQUEST A QUOTE MODAL DIALOG
   -------------------------------------------------------------------------- */
function initModal() {
  const modal = document.getElementById('rfqModal');
  const triggerBtns = document.querySelectorAll('.trigger-rfq');
  const closeBtns = document.querySelectorAll('.close-rfq');

  if (modal) {
    triggerBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
      });
    });

    closeBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        modal.classList.remove('active');
        document.body.style.overflow = '';
      });
    });

    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.classList.remove('active');
        document.body.style.overflow = '';
      }
    });
  }
}

/* --------------------------------------------------------------------------
   6. FRONTEND FORM SUBMISSION & SUCCESS STATE
   -------------------------------------------------------------------------- */
function initFormHandler() {
  const forms = document.querySelectorAll('.quote-form-handler');

  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const btn = form.querySelector('button[type="submit"]');
      const originalText = btn.innerHTML;

      btn.disabled = true;
      btn.innerHTML = 'Submitting Request...';

      setTimeout(() => {
        // Show success alert message
        alert('Thank you for your enquiry! Zhejiang Maven Industrial Technology Co., Ltd. international team will evaluate your project details and contact you within 24 business hours.');
        form.reset();
        btn.disabled = false;
        btn.innerHTML = originalText;

        const modal = document.getElementById('rfqModal');
        if (modal) {
          modal.classList.remove('active');
          document.body.style.overflow = '';
        }
      }, 1000);
    });
  });
}
