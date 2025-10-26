import asyncio
import logging
from typing import Optional
from playwright.async_api import async_playwright, Browser, BrowserContext, Page
from config import Config

logger = logging.getLogger(__name__)

class BrowserDriver:
    """Browser driver class for managing Playwright browser instances"""
    
    def __init__(self):
        self.playwright = None
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None
    
    async def start(self):
        """Start browser"""
        try:
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(
                headless=Config.BROWSER_HEADLESS
            )
            self.context = await self.browser.new_context()
            self.page = await self.context.new_page()
            
            # Set timeout
            self.page.set_default_timeout(Config.BROWSER_TIMEOUT)
            
            logger.info("Browser started successfully")
            return True
        except Exception as e:
            logger.error(f"Failed to start browser: {e}")
            return False
    
    async def navigate_to(self, url: str) -> bool:
        """Navigate to specified URL"""
        try:
            if not self.page:
                raise Exception("Page not initialized")
            
            # Use domcontentloaded instead of networkidle to avoid timeout
            await self.page.goto(url, wait_until="domcontentloaded", timeout=60000)
            logger.info(f"Successfully navigated to: {url}")
            return True
        except Exception as e:
            logger.error(f"Navigation failed: {e}")
            # Even if timeout, try to continue execution
            try:
                await self.page.wait_for_load_state("domcontentloaded", timeout=10000)
                logger.info("Page loaded successfully")
                return True
            except:
                pass
            return False
    
    async def click_element(self, selector: str) -> bool:
        """Click element"""
        try:
            if not self.page:
                raise Exception("Page not initialized")
            
            await self.page.click(selector)
            logger.info(f"Successfully clicked element: {selector}")
            return True
        except Exception as e:
            logger.error(f"Failed to click element: {e}")
            return False
    
    async def type_text(self, selector: str, text: str) -> bool:
        """Type text"""
        try:
            if not self.page:
                raise Exception("Page not initialized")
            
            await self.page.fill(selector, text)
            logger.info(f"Successfully typed text to: {selector}")
            return True
        except Exception as e:
            logger.error(f"Failed to type text: {e}")
            return False
    
    async def get_text(self, selector: str) -> Optional[str]:
        """Get element text"""
        try:
            if not self.page:
                raise Exception("Page not initialized")
            
            text = await self.page.text_content(selector)
            logger.info(f"Successfully got text from: {selector}")
            return text
        except Exception as e:
            logger.error(f"Failed to get text: {e}")
            return None
    
    async def wait_for_element(self, selector: str, timeout: int = 5000) -> bool:
        """Wait for element to appear"""
        try:
            if not self.page:
                raise Exception("Page not initialized")
            
            await self.page.wait_for_selector(selector, timeout=timeout)
            logger.info(f"Element appeared: {selector}")
            return True
        except Exception as e:
            logger.error(f"Wait for element timeout: {e}")
            return False
    
    async def take_screenshot(self, path: str = "screenshot.png") -> bool:
        """Take screenshot"""
        try:
            if not self.page:
                raise Exception("Page not initialized")
            
            await self.page.screenshot(path=path)
            logger.info(f"Screenshot saved to: {path}")
            return True
        except Exception as e:
            logger.error(f"Screenshot failed: {e}")
            return False
    
    async def close(self):
        """Close browser"""
        try:
            if self.context:
                await self.context.close()
            if self.browser:
                await self.browser.close()
            if self.playwright:
                await self.playwright.stop()
            logger.info("Browser closed")
        except Exception as e:
            logger.error(f"Failed to close browser: {e}")
