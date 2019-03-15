" Helps plugins load correctly
filetype plugin indent on

"Start plugin system.
call plug#begin()

" Autocompletion
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }

" Autocompletion of Python
Plug 'zchee/deoplete-jedi'

" Use jedi-vim instead of deoplete
Plug 'davidhalter/jedi-vim'

" Code snippets
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'

" Tab completion - probably not needed any more with deoplete
Plug 'ervandew/supertab'

" Color themes
Plug 'flazz/vim-colorschemes'

" Like a TOC for code
Plug 'vim-scripts/taglist.vim'

" More ctag goodness
Plug 'xolox/vim-easytags'

" easytags requires vim-misc
Plug 'xolox/vim-misc'

" Cross-file search and replace
Plug 'brooth/far.vim'

" Status bar mods
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" Display git differences
Plug 'airblade/vim-gitgutter'

" Syntax checking
Plug 'vim-syntastic/syntastic'

" Code folding
Plug 'tmhedberg/SimpylFold'

call plug#end()

" Configure basic behaviors.
set nocompatible
set fileformat=unix
set encoding=utf-8

" Set split defaults to right and bottom
set splitbelow
set splitright

" Syntax highlighting
syntax enable
syntax on

" Line numbers
set number
set relativenumber

" Code folding
set foldcolumn=3

" Save view when file is saved, load view when file is loaded.
autocmd BufWinLeave * mkview
autocmd BufWinEnter * silent loadview
" the following line keeps the current working directory from being saved (and
" then loaded) in the view.
set viewoptions-=options

set title

" Indentation, tab stops
set ts=4
set autoindent
set expandtab
set shiftwidth=4

set cursorline
set ruler
set showmatch

" Text wrap column
set tw=79
set cc=+1

" Persistent undo
set undodir=~/.vim/undodir
set undofile

" Set autocomplete behavior. Commented out for jedi-vim
"set completeopt=menuone,preview

" Key remappings
nnoremap <esc> :noh<return><esc>

" Plugin Configurations

" Let plugins show effects after 250ms, not 4s
set updatetime=250

" Set color scheme
colorscheme zenburn

" Deoplete enable
let g:deoplete#enable_at_startup = 1
" Disable Jedi auto-complete
let g:jedi#completions_enabled = 0

" Enable Deoplete logging
"let g:deoplete#enable_profile = 1
"call deoplete#enable_logging('DEBUG', 'deoplete.log')
"call deoplete#custom#set('jedi', 'debug_enabled', 1)

if !exists('g:deoplete#omni#input_patterns')
    let g:deoplete#omni#input_patterns = {}
endif

" Close preview window after complete
"autocmd InsertLeave,CompleteDone * if pumvisible() == 0 | pclose | endif

" Deoplete tab-completion
inoremap <expr><tab> pumvisible() ? "\<c-n" : "\<tab>"

" Deoplete-jedi enable docstring preview
let g:deoplete#sources#jedi#show_docstring = 1

" Force it to use Python 3 instead of 2
" This was commented out so that whatever python exists in a virtualenv would
" be the one used by deoplete.
" let g:deoplete#sources#jedi#python_path = "/usr/bin/python3"

" Define SimpylFold behavior.
let g:SimpylFold_docstring_preview = 1

" Configure airline status bar
let g:airline_powerline_fonts=1
let g:airline_theme='wombat'

" Let vim-gitgutter work better with large files
let g:gitgutter_max_signs=10000

" Syntastic general settings
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

" Syntastic checker selection
let g:syntastic_python_checkers = ['flake8']
