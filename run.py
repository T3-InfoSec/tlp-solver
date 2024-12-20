import asyncio
import logging
from app import create_app, logger

if __name__ == "__main__":
    app = create_app()

    async def main():
        try:
            logger.info("Starting SolverClientApp...")
            await app.start()
        except KeyboardInterrupt:
            logger.info("Application terminated by user.")
            await app.stop()
        except Exception as e:
            logger.error(f"An unexpected error occurred: {str(e)}")
            await app.stop()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Application stopped.")
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
