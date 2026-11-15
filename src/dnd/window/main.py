import pygame
import pygame_gui

from ..engine.main import start


WINDOW_SIZE = (800, 600)


def main() -> None:
    pygame.init()
    pygame.display.set_caption("DnD")

    window_surface = pygame.display.set_mode(WINDOW_SIZE)
    background = pygame.Surface(WINDOW_SIZE)
    background.fill(pygame.Color("#1a1a1a"))

    manager = pygame_gui.UIManager(WINDOW_SIZE)

    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((50, 30), (700, 40)),
        text="Character Roller",
        manager=manager,
    )

    roll_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 90), (160, 45)),
        text="Roll Character",
        manager=manager,
    )

    results = pygame_gui.elements.UITextBox(
        html_text="Press Roll Character to generate stats.",
        relative_rect=pygame.Rect((50, 160), (700, 380)),
        manager=manager,
    )

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:  # noqa: SIM102
                if event.ui_element == roll_button:


                    lines = []

                    while (roll := start()) is not None:
                        lines.append(
                            f"<b>{roll["category"]}</b>: {roll['tag']}"
                        )


                    results.set_text("<br>".join(lines))

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
