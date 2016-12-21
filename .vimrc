set nocompatible " no idea what this does?
filetype off     " also no idea

" enable syntax highlighting
syntax enable
syntax on

" show line numbers (standard and relative)
set number
set relativenumber

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

" enable all Python syntax highlighting features
let python_highlight_all = 1


" Vundle configuration
" Set the runtime path to include Vundle, and
" then initialize it.
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle - required
Plugin 'gmarik/Vundle.vim'

" Add other plugins here

Plugin 'davidhalter/jedi-vim'

Plugin 'ervandew/supertab'

Plugin 'tmhedberg/SimpylFold'
let g:SimpylFold_docstring_preview=1 " see docstrings for folded code
" Enable folding with spacebar
nnoremap <space> za
set foldmethod=indent
set foldlevel=99

" Better conform to PEP8 standard indentation
Plugin 'vim-scripts/indentpython.vim'

" Plugin which checks syntax on save
Plugin 'scrooloose/syntastic'

" Plugin which checks PEP8
Plugin 'nvie/vim-flake8'

" Plugins which add color schemes
Plugin 'jnurmine/Zenburn'
Plugin 'altercation/vim-colors-solarized'

" File tree for browsing source folder(s)
Plugin 'scrooloose/nerdtree'
Plugin 'jistr/vim-nerdtree-tabs'
let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree
" autocmd vimenter * NERDTree "automatically open NERDtree
map <C-n> :NERDTreeToggle<CR>

" Search for basically anything from vim
Plugin 'kien/ctrlp.vim'

" Perform basic git commands within vim
Plugin 'tpope/vim-fugitive'

" Status bar
Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}

Plugin 'dhruvasagar/vim-table-mode'

" Supposed to allow || to enable Table Mode in insert mode - doesn't work?
function! s:isAtStartOfLine(mapping)
      let text_before_cursor = getline('.')[0 : col('.')-1]
        let mapping_pattern = '\V' . escape(a:mapping, '\')
          let comment_pattern = '\V' . escape(substitute(&l:commentstring, '%s.*$', '', ''), '\')
            return (text_before_cursor =~? '^' . ('\v(' . comment_pattern . '\v)?') . '\s*\v' . mapping_pattern . '\v$')
        endfunction

        inoreabbrev <expr> <bar><bar>
                  \ <SID>isAtStartOfLine('\|\|') ?
                  \ '<c-o>:TableModeEnable<cr><bar><space><bar><left><left>' : '<bar><bar>'
        inoreabbrev <expr> __
                  \ <SID>isAtStartOfLine('__') ?
                  \ '<c-o>:silent! TableModeDisable<cr>' : '__'

" Format Tables in ReST
let g:table_mode_corner_corner="+"
let g:table_mode_header_fillchar="="

" All Vundle plugins must be added before the following line
call vundle#end()

filetype plugin indent on

" enable omni completion
" set omnifunc=syntaxcomplete#Complete


" set format to UNIX to avoid conversion issues with github
set fileformat=unix
" set encoding to Unicode
set encoding=utf-8

" set the color scheme
if has('gui_running')
    set background=dark
    colorscheme solarized
else
    colorscheme zenburn
endif

call togglebg#map("<F5>")

