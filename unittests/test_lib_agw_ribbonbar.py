import unittest
from unittests import wtc
import wx

import wx.lib.agw.ribbon as RB
from wx.lib.embeddedimage import PyEmbeddedImage

#---------------------------------------------------------------------------
align_center = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAABAAAAAPCAYAAADtc08vAAAABHNCSVQICAgIfAhkiAAAADpJ"
    b"REFUKJFjZGRiZqAEMFGkm4GBgQWZ8//f3//EaGJkYmaEsyn1Ags2QVwuQbaZNi4YDYMRGwYU"
    b"ZyYAopsYTgbXQz4AAAAASUVORK5CYII=")

#----------------------------------------------------------------------
align_left = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAABAAAAAPCAYAAADtc08vAAAABHNCSVQICAgIfAhkiAAAADxJ"
    b"REFUKJFjZGRiZqAEMFGkm4GBgYWBgYHh/7+//4lRzMjEzIghRqkX8LoAm430dQExLhoNg2ER"
    b"BhRnJgDCqhhOM7rMkQAAAABJRU5ErkJggg==")

ribbon = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAYxJ"
    b"REFUOI19krtKA0EUhr8xMcYbRIJgk87KBSsRBK0UROMi6y3Wig+wpLQTLMUHsLNSBEVCIoKd"
    b"gpAyEBBMISKIiDeSmLhqxiLuZrPjeqrhXH6+c/4RoiWAX2iGKQHyR9vCryf43+D4zBLWtwTw"
    b"FRJeAs0wpbEQ5+4Jql8BIl1tTu385EARCXqHB0bihIKwuxH+zdZY2xQIIRibWgSQbpEWL1Jf"
    b"j+S5VH/ryQp6ssLOuvS5gItAM0w5ObtMb1eRd6ueS221O0JVq41wKKhQOAT5o21xerzHQ7GV"
    b"SGeDwI630ge1mlTuoKzQHQ5RsRppPVkhtdVOTcJb+UNZ4U8XVlfmuX385LX0xUu5UStkM4oL"
    b"ioAtAqDP6Vzff3N1mXHW9PYqH0kzTDk0bhDpCJE63AdgQk/wWr+s/JdAM0zZPzzt4E7oCQDO"
    b"Uvu4826RJhsHR+O8Ww3Pbx6KynqDo/EmkiYbcxdpYlFBIZtRBgvZDLGoIHeR/pvAFrHVNcOU"
    b"sWi9r+Cp+d7AHbYTHnElfgAFJbH0Sf7mkQAAAABJRU5ErkJggg==")

def CreateBitmap(xpm):

    bmp = eval(xpm).Bitmap

    return bmp

class lib_agw_ribbon_Tests(wtc.WidgetTestCase):

    def setUp(self):
        super(lib_agw_ribbon_Tests, self).setUp()

        self.realRibbonGalleryOnPaint = RB.RibbonGallery.OnPaint
        def MonkeyPatchedOnPaint(self, event): pass
        RB.RibbonGallery.OnPaint = MonkeyPatchedOnPaint

        self.realRibbonGalleryLayout = RB.RibbonGallery.Layout
        def MonkeyPatchedLayout(self): return False
        RB.RibbonGallery.Layout = MonkeyPatchedLayout

    def tearDown(self):
        super(lib_agw_ribbon_Tests, self).tearDown()
        RB.RibbonGallery.OnPaint = self.realRibbonGalleryOnPaint
        RB.RibbonGallery.Layout = self.realRibbonGalleryLayout

    def test_lib_agw_ribbonCtor(self):
        rib = RB.RibbonBar(self.frame, wx.ID_ANY, agwStyle=RB.RIBBON_BAR_DEFAULT_STYLE|RB.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS)

        home = RB.RibbonPage(rib, wx.ID_ANY, "Examples", CreateBitmap("ribbon"))
        toolbar_panel = RB.RibbonPanel(home, wx.ID_ANY, "Toolbar", wx.NullBitmap, wx.DefaultPosition,
                                       wx.DefaultSize, agwStyle=RB.RIBBON_PANEL_NO_AUTO_MINIMISE)

        toolbar = RB.RibbonToolBar(toolbar_panel, wx.ID_ANY)
        toolbar.AddTool(wx.ID_ANY, CreateBitmap("align_left"))
        toolbar.AddTool(wx.ID_ANY, CreateBitmap("align_center"))
        toolbar.AddSeparator()
        toolbar.AddHybridTool(wx.ID_NEW, wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_OTHER, wx.Size(16, 15)))
        toolbar.AddSeparator()
        toolbar.AddDropdownTool(wx.ID_UNDO, wx.ArtProvider.GetBitmap(wx.ART_UNDO, wx.ART_OTHER, wx.Size(16, 15)))

    def test_lib_agw_ribbonControlCtor(self):
        rib = RB.RibbonBar(self.frame, wx.ID_ANY, agwStyle=RB.RIBBON_BAR_DEFAULT_STYLE|RB.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS)
        RB.RibbonControl(rib)

    def test_lib_agw_ribbonGalleryCtor(self):
        rib = RB.RibbonBar(self.frame, wx.ID_ANY, agwStyle=RB.RIBBON_BAR_DEFAULT_STYLE|RB.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS)
        page = RB.RibbonPage(rib, wx.ID_ANY, "Appearance")
        primary_panel = RB.RibbonPanel(page, wx.ID_ANY, "Primary Colour")
        RB.RibbonGallery(primary_panel)

    def test_lib_agw_ribbonPageCtor(self):
        rib = RB.RibbonBar(self.frame, wx.ID_ANY, agwStyle=RB.RIBBON_BAR_DEFAULT_STYLE|RB.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS)
        RB.RibbonPage(rib)

    def test_lib_agw_ribbonPanelCtor(self):
        rib = RB.RibbonBar(self.frame, wx.ID_ANY, agwStyle=RB.RIBBON_BAR_DEFAULT_STYLE|RB.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS)
        page = RB.RibbonPage(rib, wx.ID_ANY, "Appearance")
        RB.RibbonPanel(page)

    def test_lib_agw_ribbonArtProviders(self):
        rib = RB.RibbonBar(self.frame, wx.ID_ANY, agwStyle=RB.RIBBON_BAR_DEFAULT_STYLE|RB.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS)
        rib.SetArtProvider(RB.RibbonDefaultArtProvider())
        rib.SetArtProvider(RB.RibbonAUIArtProvider())
        rib.SetArtProvider(RB.RibbonMSWArtProvider())
        rib.SetArtProvider(RB.RibbonOSXArtProvider())

    def test_lib_agw_ribbonEvents(self):
        RB.EVT_RIBBONBAR_PAGE_CHANGED
        RB.EVT_RIBBONBAR_PAGE_CHANGING
        RB.EVT_RIBBONBAR_TAB_LEFT_DCLICK
        RB.EVT_RIBBONBAR_TAB_MIDDLE_DOWN
        RB.EVT_RIBBONBAR_TAB_MIDDLE_UP
        RB.EVT_RIBBONBAR_TAB_RIGHT_DOWN
        RB.EVT_RIBBONBAR_TAB_RIGHT_UP
        RB.EVT_RIBBONBUTTONBAR_CLICKED
        RB.EVT_RIBBONGALLERY_HOVER_CHANGED
        RB.EVT_RIBBONGALLERY_SELECTED
        RB.EVT_RIBBONPANEL_EXTBUTTON_ACTIVATED
        RB.EVT_RIBBONTOOLBAR_CLICKED
        RB.EVT_RIBBONTOOLBAR_DROPDOWN_CLICKED

    def test_lib_agw_ribbonStyles(self):
        RB.RIBBON_BAR_DEFAULT_STYLE
        RB.RIBBON_BAR_FOLDBAR_STYLE
        RB.RIBBON_BAR_SHOW_PAGE_LABELS
        RB.RIBBON_BAR_SHOW_PAGE_ICONS
        RB.RIBBON_BAR_FLOW_HORIZONTAL
        RB.RIBBON_BAR_FLOW_VERTICAL
        RB.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS
        RB.RIBBON_BAR_SHOW_PANEL_MINIMISE_BUTTONS
        RB.RIBBON_BAR_ALWAYS_SHOW_TABS

    def test_lib_agw_pyprogressConstantsExists(self):
        RB.RIBBON_ART_TAB_SEPARATION_SIZE
        RB.RIBBON_ART_PAGE_BORDER_LEFT_SIZE
        RB.RIBBON_ART_PAGE_BORDER_TOP_SIZE
        RB.RIBBON_ART_PAGE_BORDER_RIGHT_SIZE
        RB.RIBBON_ART_PAGE_BORDER_BOTTOM_SIZE
        RB.RIBBON_ART_PANEL_X_SEPARATION_SIZE
        RB.RIBBON_ART_PANEL_Y_SEPARATION_SIZE
        RB.RIBBON_ART_TOOL_GROUP_SEPARATION_SIZE
        RB.RIBBON_ART_GALLERY_BITMAP_PADDING_LEFT_SIZE
        RB.RIBBON_ART_GALLERY_BITMAP_PADDING_RIGHT_SIZE
        RB.RIBBON_ART_GALLERY_BITMAP_PADDING_TOP_SIZE
        RB.RIBBON_ART_GALLERY_BITMAP_PADDING_BOTTOM_SIZE
        RB.RIBBON_ART_PANEL_LABEL_FONT
        RB.RIBBON_ART_BUTTON_BAR_LABEL_FONT
        RB.RIBBON_ART_TAB_LABEL_FONT
        RB.RIBBON_ART_BUTTON_BAR_LABEL_COLOUR
        RB.RIBBON_ART_BUTTON_BAR_HOVER_BORDER_COLOUR
        RB.RIBBON_ART_BUTTON_BAR_HOVER_BACKGROUND_TOP_COLOUR
        RB.RIBBON_ART_BUTTON_BAR_HOVER_BACKGROUND_TOP_GRADIENT_COLOUR
        RB.RIBBON_ART_BUTTON_BAR_HOVER_BACKGROUND_COLOUR
        RB.RIBBON_ART_BUTTON_BAR_HOVER_BACKGROUND_GRADIENT_COLOUR
        RB.RIBBON_ART_BUTTON_BAR_ACTIVE_BORDER_COLOUR
        RB.RIBBON_ART_BUTTON_BAR_ACTIVE_BACKGROUND_TOP_COLOUR
        RB.RIBBON_ART_BUTTON_BAR_ACTIVE_BACKGROUND_TOP_GRADIENT_COLOUR
        RB.RIBBON_ART_BUTTON_BAR_ACTIVE_BACKGROUND_COLOUR
        RB.RIBBON_ART_BUTTON_BAR_ACTIVE_BACKGROUND_GRADIENT_COLOUR
        RB.RIBBON_ART_GALLERY_BORDER_COLOUR
        RB.RIBBON_ART_GALLERY_HOVER_BACKGROUND_COLOUR
        RB.RIBBON_ART_GALLERY_BUTTON_BACKGROUND_COLOUR
        RB.RIBBON_ART_GALLERY_BUTTON_BACKGROUND_GRADIENT_COLOUR
        RB.RIBBON_ART_GALLERY_BUTTON_BACKGROUND_TOP_COLOUR
        RB.RIBBON_ART_GALLERY_BUTTON_FACE_COLOUR
        RB.RIBBON_ART_GALLERY_BUTTON_HOVER_BACKGROUND_COLOUR
        RB.RIBBON_ART_GALLERY_BUTTON_HOVER_BACKGROUND_GRADIENT_COLOUR
        RB.RIBBON_ART_GALLERY_BUTTON_HOVER_BACKGROUND_TOP_COLOUR
        RB.RIBBON_ART_GALLERY_BUTTON_HOVER_FACE_COLOUR
        RB.RIBBON_ART_GALLERY_BUTTON_ACTIVE_BACKGROUND_COLOUR
        RB.RIBBON_ART_GALLERY_BUTTON_ACTIVE_BACKGROUND_GRADIENT_COLOUR
        RB.RIBBON_ART_GALLERY_BUTTON_ACTIVE_BACKGROUND_TOP_COLOUR
        RB.RIBBON_ART_GALLERY_BUTTON_ACTIVE_FACE_COLOUR
        RB.RIBBON_ART_GALLERY_BUTTON_DISABLED_BACKGROUND_COLOUR
        RB.RIBBON_ART_GALLERY_BUTTON_DISABLED_BACKGROUND_GRADIENT_COLOUR
        RB.RIBBON_ART_GALLERY_BUTTON_DISABLED_BACKGROUND_TOP_COLOUR
        RB.RIBBON_ART_GALLERY_BUTTON_DISABLED_FACE_COLOUR
        RB.RIBBON_ART_GALLERY_ITEM_BORDER_COLOUR
        RB.RIBBON_ART_TAB_LABEL_COLOUR
        RB.RIBBON_ART_TAB_SEPARATOR_COLOUR
        RB.RIBBON_ART_TAB_SEPARATOR_GRADIENT_COLOUR
        RB.RIBBON_ART_TAB_CTRL_BACKGROUND_COLOUR
        RB.RIBBON_ART_TAB_CTRL_BACKGROUND_GRADIENT_COLOUR
        RB.RIBBON_ART_TAB_HOVER_BACKGROUND_TOP_COLOUR
        RB.RIBBON_ART_TAB_HOVER_BACKGROUND_TOP_GRADIENT_COLOUR
        RB.RIBBON_ART_TAB_HOVER_BACKGROUND_COLOUR
        RB.RIBBON_ART_TAB_HOVER_BACKGROUND_GRADIENT_COLOUR
        RB.RIBBON_ART_TAB_ACTIVE_BACKGROUND_TOP_COLOUR
        RB.RIBBON_ART_TAB_ACTIVE_BACKGROUND_TOP_GRADIENT_COLOUR
        RB.RIBBON_ART_TAB_ACTIVE_BACKGROUND_COLOUR
        RB.RIBBON_ART_TAB_ACTIVE_BACKGROUND_GRADIENT_COLOUR
        RB.RIBBON_ART_TAB_BORDER_COLOUR
        RB.RIBBON_ART_PANEL_BORDER_COLOUR
        RB.RIBBON_ART_PANEL_BORDER_GRADIENT_COLOUR
        RB.RIBBON_ART_PANEL_MINIMISED_BORDER_COLOUR
        RB.RIBBON_ART_PANEL_MINIMISED_BORDER_GRADIENT_COLOUR
        RB.RIBBON_ART_PANEL_LABEL_BACKGROUND_COLOUR
        RB.RIBBON_ART_PANEL_LABEL_BACKGROUND_GRADIENT_COLOUR
        RB.RIBBON_ART_PANEL_LABEL_COLOUR
        RB.RIBBON_ART_PANEL_HOVER_LABEL_BACKGROUND_COLOUR
        RB.RIBBON_ART_PANEL_HOVER_LABEL_BACKGROUND_GRADIENT_COLOUR
        RB.RIBBON_ART_PANEL_HOVER_LABEL_COLOUR
        RB.RIBBON_ART_PANEL_MINIMISED_LABEL_COLOUR
        RB.RIBBON_ART_PANEL_ACTIVE_BACKGROUND_TOP_COLOUR
        RB.RIBBON_ART_PANEL_ACTIVE_BACKGROUND_TOP_GRADIENT_COLOUR
        RB.RIBBON_ART_PANEL_ACTIVE_BACKGROUND_COLOUR
        RB.RIBBON_ART_PANEL_ACTIVE_BACKGROUND_GRADIENT_COLOUR
        RB.RIBBON_ART_PANEL_BUTTON_FACE_COLOUR
        RB.RIBBON_ART_PANEL_BUTTON_HOVER_FACE_COLOUR
        RB.RIBBON_ART_PAGE_BORDER_COLOUR
        RB.RIBBON_ART_PAGE_BACKGROUND_TOP_COLOUR
        RB.RIBBON_ART_PAGE_BACKGROUND_TOP_GRADIENT_COLOUR
        RB.RIBBON_ART_PAGE_BACKGROUND_COLOUR
        RB.RIBBON_ART_PAGE_BACKGROUND_GRADIENT_COLOUR
        RB.RIBBON_ART_PAGE_HOVER_BACKGROUND_TOP_COLOUR
        RB.RIBBON_ART_PAGE_HOVER_BACKGROUND_TOP_GRADIENT_COLOUR
        RB.RIBBON_ART_PAGE_HOVER_BACKGROUND_COLOUR
        RB.RIBBON_ART_PAGE_HOVER_BACKGROUND_GRADIENT_COLOUR
        RB.RIBBON_ART_TOOLBAR_BORDER_COLOUR
        RB.RIBBON_ART_TOOLBAR_HOVER_BORDER_COLOUR
        RB.RIBBON_ART_TOOLBAR_FACE_COLOUR
        RB.RIBBON_ART_TOOL_BACKGROUND_TOP_COLOUR
        RB.RIBBON_ART_TOOL_BACKGROUND_TOP_GRADIENT_COLOUR
        RB.RIBBON_ART_TOOL_BACKGROUND_COLOUR
        RB.RIBBON_ART_TOOL_BACKGROUND_GRADIENT_COLOUR
        RB.RIBBON_ART_TOOL_HOVER_BACKGROUND_TOP_COLOUR
        RB.RIBBON_ART_TOOL_HOVER_BACKGROUND_TOP_GRADIENT_COLOUR
        RB.RIBBON_ART_TOOL_HOVER_BACKGROUND_COLOUR
        RB.RIBBON_ART_TOOL_HOVER_BACKGROUND_GRADIENT_COLOUR
        RB.RIBBON_ART_TOOL_ACTIVE_BACKGROUND_TOP_COLOUR
        RB.RIBBON_ART_TOOL_ACTIVE_BACKGROUND_TOP_GRADIENT_COLOUR
        RB.RIBBON_ART_TOOL_ACTIVE_BACKGROUND_COLOUR
        RB.RIBBON_ART_TOOL_ACTIVE_BACKGROUND_GRADIENT_COLOUR

        # RibbonScrollButtonStyle
        RB.RIBBON_SCROLL_BTN_LEFT
        RB.RIBBON_SCROLL_BTN_RIGHT
        RB.RIBBON_SCROLL_BTN_UP
        RB.RIBBON_SCROLL_BTN_DOWN
        RB.RIBBON_SCROLL_BTN_DIRECTION_MASK
        RB.RIBBON_SCROLL_BTN_NORMAL
        RB.RIBBON_SCROLL_BTN_HOVERED
        RB.RIBBON_SCROLL_BTN_ACTIVE
        RB.RIBBON_SCROLL_BTN_STATE_MASK
        RB.RIBBON_SCROLL_BTN_FOR_OTHER
        RB.RIBBON_SCROLL_BTN_FOR_TABS
        RB.RIBBON_SCROLL_BTN_FOR_PAGE
        RB.RIBBON_SCROLL_BTN_FOR_MASK

        # RibbonButtonKind
        RB.RIBBON_BUTTON_NORMAL
        RB.RIBBON_BUTTON_DROPDOWN
        RB.RIBBON_BUTTON_HYBRID
        RB.RIBBON_BUTTON_TOGGLE

        # RibbonButtonBarButtonState
        RB.RIBBON_BUTTONBAR_BUTTON_SMALL
        RB.RIBBON_BUTTONBAR_BUTTON_MEDIUM
        RB.RIBBON_BUTTONBAR_BUTTON_LARGE
        RB.RIBBON_BUTTONBAR_BUTTON_SIZE_MASK
        RB.RIBBON_BUTTONBAR_BUTTON_NORMAL_HOVERED
        RB.RIBBON_BUTTONBAR_BUTTON_DROPDOWN_HOVERED
        RB.RIBBON_BUTTONBAR_BUTTON_HOVER_MASK
        RB.RIBBON_BUTTONBAR_BUTTON_NORMAL_ACTIVE
        RB.RIBBON_BUTTONBAR_BUTTON_DROPDOWN_ACTIVE
        RB.RIBBON_BUTTONBAR_BUTTON_ACTIVE_MASK
        RB.RIBBON_BUTTONBAR_BUTTON_DISABLED
        RB.RIBBON_BUTTONBAR_BUTTON_TOGGLED
        RB.RIBBON_BUTTONBAR_BUTTON_STATE_MASK

        # RibbonGalleryButtonState
        RB.RIBBON_GALLERY_BUTTON_NORMAL
        RB.RIBBON_GALLERY_BUTTON_HOVERED
        RB.RIBBON_GALLERY_BUTTON_ACTIVE
        RB.RIBBON_GALLERY_BUTTON_DISABLED


        RB.RIBBON_BAR_SHOW_PAGE_LABELS
        RB.RIBBON_BAR_SHOW_PAGE_ICONS
        RB.RIBBON_BAR_FLOW_HORIZONTAL
        RB.RIBBON_BAR_FLOW_VERTICAL
        RB.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS
        RB.RIBBON_BAR_SHOW_PANEL_MINIMISE_BUTTONS
        RB.RIBBON_BAR_ALWAYS_SHOW_TABS
        RB.RIBBON_BAR_DEFAULT_STYLE
        RB.RIBBON_BAR_FOLDBAR_STYLE

        RB.RIBBON_TOOLBAR_TOOL_FIRST
        RB.RIBBON_TOOLBAR_TOOL_LAST
        RB.RIBBON_TOOLBAR_TOOL_POSITION_MASK
        RB.RIBBON_TOOLBAR_TOOL_NORMAL_HOVERED
        RB.RIBBON_TOOLBAR_TOOL_DROPDOWN_HOVERED
        RB.RIBBON_TOOLBAR_TOOL_HOVER_MASK
        RB.RIBBON_TOOLBAR_TOOL_NORMAL_ACTIVE
        RB.RIBBON_TOOLBAR_TOOL_DROPDOWN_ACTIVE
        RB.RIBBON_TOOLBAR_TOOL_ACTIVE_MASK
        RB.RIBBON_TOOLBAR_TOOL_DISABLED
        RB.RIBBON_TOOLBAR_TOOL_TOGGLED
        RB.RIBBON_TOOLBAR_TOOL_STATE_MASK

        RB.RIBBON_PANEL_NO_AUTO_MINIMISE
        RB.RIBBON_PANEL_EXT_BUTTON
        RB.RIBBON_PANEL_MINIMISE_BUTTON
        RB.RIBBON_PANEL_STRETCH
        RB.RIBBON_PANEL_FLEXIBLE

        RB.RIBBON_PANEL_DEFAULT_STYLE

#---------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()


