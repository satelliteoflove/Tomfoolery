#/usr/bin/env python3

"""UI based in Asciimatics (https://github.com/peterbrittain/asciimatics)."""

from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
        Button, TextBox, Widget
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, \
        StopApplication
from actors import actors
from config.config import load_config

character_list = []

class CharacterView(Frame):
    def __init__(self, screen, actor_list):
        """Main menu. Create, Delete, Edit and View Characters.

        :screen: asciimatics screen to be used.
        :actor_list: iterable with Actor objects in it.
        """

        super(CharacterView, self).__init__(screen,
                                            screen.height * 2 // 3,
                                            screen.width * 2 // 3,
                                            on_load=self._reload_list,
                                            hover_focus=True,
                                            can_scroll=False,
                                            title="Character List")
        # Load/Save from global actor list.
        self._actor_list = actor_list

        # Create the form for displaying the list of characters.
        self._list_view = ListBox(
                Widget.FILL_FRAME,
                self._actor_list,
                name="Characters",
                add_scroll_bar=True,
                on_change=self._on_pick,
                on_select=self._edit)
        self._edit_button = Button("Edit", self.edit)
        self._delete_button = Button("Delete", self.delete)
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(self._list_view)
        layout.add_widget(Divider())
        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Create", self._create), 0)
        layout2.add_widget(self._edit_button, 1)
        layout2.add_widget(self._delete_button, 2)
        layout2.add_widget(Button("Quit", self._quit), 3)
        self.fix()
        self._on_pick()

    def _on_pick(self):
        self._edit_button.disabled = self._list_view.value is None
        self._delete_button.disabled = self._list_view.value is None

    def _reload_list(self, new_value=None):
        self._list_view.options = self._actor_list
        self._list_view.value = new_value

    def _create(self):
        self._actor_list
