set nocompatible " no idea what this does?
filetype off     " also no idea

" enable syntax highlighting
syntax enable
syntax on

" show line numbers (standard and relative) and add a foldcolumn
set number
set relativenumber
set foldcolumn=3

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
set wrapmargin=3
set tw=80

" stop automatic insertion of newline character at 80 lines
" set tw=0

" enable all Python syntax highlighting features
let python_highlight_all = 1

" Add vertical bar at 80 columns
if exists('+colorcolumn')
      set colorcolumn=80
  else
        au BufWinEnter * let w:m2=matchadd('ErrorMsg', '\%>80v.\+', -1)
    endif

filetype plugin indent on

" enable omni completion
" set omnifunc=syntaxcomplete#Complete


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


"call togglebg#map("<F5>")

call plug#begin()
Plug 'roxma/nvim-completion-manager'
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'
Plug 'ervandew/supertab'
Plug 'flazz/vim-colorschemes'
Plug 'vim-scripts/taglist.vim'
call plug#end()

" set the color scheme
if has('gui_running')
    set background=dark
    colorscheme desert
    set guifont=Monospace\ 14
    set guioptions-=T "remove toolbar
else
    colorscheme zenburn
endif
