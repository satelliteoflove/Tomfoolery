"Start plugin system.
call plug#begin()
"Autocompletion
Plug 'roxma/nvim-completion-manager'
"Plug 'davidhalter/jedi-vim'
" Code snippets
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'
" Tab completion
Plug 'ervandew/supertab'
" Color themes
Plug 'flazz/vim-colorschemes'
" Like a TOC for code
Plug 'vim-scripts/taglist.vim'
" Cross-file search and replace
Plug 'brooth/far.vim'
" Status bar mods
Plug 'bling/vim-airline'
Plug 'airblade/vim-gitgutter'
Plug 'vim-syntastic/syntastic'
Plug 'tmhedberg/SimpylFold'
call plug#end()

set nocompatible " Disregards backwards compatibility with vi.

" enable syntax highlighting
syntax enable
syntax on

" show line numbers (standard and relative) and add a foldcolumn
set number
set relativenumber
set foldcolumn=3

" Define SimpylFold behavior.
let g:SimpylFold_docstring_preview = 1

" Automatically save and load views (save folds).
autocmd BufWinLeave * mkview
autocmd BufWinEnter * silent! loadview

" Know what you're editing
set title

" set tabs to instead insert 4 spaces
set ts=4

" indent when moving to the next line while writing code
set autoindent

" expand tabs into spaces
set expandtab

" when using the >> or << commands, shift lines by 4 spaces
set shiftwidth=4

" show a visual line under the cursor's current line
set cursorline

" show the matching part of the pair for [], {} and ()
set showmatch

" set wrap margin in # of chars from the right margin
set wrapmargin=1
set tw=80

" Add vertical bar at 80 columns
if exists('+colorcolumn')
      set colorcolumn=80
  else
        au BufWinEnter * let w:m2=matchadd('ErrorMsg', '\%>80v.\+', -1)
    endif

filetype plugin indent on

" set format to UNIX to avoid conversion issues with github
set fileformat=unix
" set encoding to Unicode
set encoding=utf-8

function! TwiddleCase(str)
  if a:str ==# toupper(a:str)
    let result = tolower(a:str)
  elseif a:str ==# tolower(a:str)
    let result = substitute(a:str,'\(\<\w\+\>\)', '\u\1', 'g')
  else
    let result = toupper(a:str)
  endif
  return result
endfunction
vnoremap ~ y:call setreg('', TwiddleCase(@"), getregtype(''))<CR>gv""Pgv

" Always show status bar
set laststatus=2

" Let plugins show effects after 500ms, not 4s
set updatetime=500

" Change autocomplete behavior
set completeopt=menuone,preview,noinsert


" Let vim-gitgutter work better with large files
let g:gitgutter_max_signs=10000

colorscheme zenburn

" Turn off sounds and enable a 'visual' bell.
set visualbell t_vb=
au GuiEnter * set visualbell t_vb=

" Clear search buffer (clears the last search highlights)
nnoremap <F10> :let @/=""<CR>

" Highlight keywords in comments like TODO, FIXME, WARNING, NOTE
augroup highlight_keyword
    autocmd!
    autocmd WinEnter,VimEnter * :silent! call matchadd('Todo', 'TODO\|FIXME\|WARNING\|NOTE\|Plugin:', -1)
augroup END

" Use 'true color' in terminal
set termguicolors

" The guicursor functionality in Neovim causes problems in some terminal
" emulators.
set guicursor=
" Workaround some broken plugins which set guicursor indiscriminately.
autocmd OptionSet guicursor noautocmd set guicursor=
