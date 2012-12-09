# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pagenote
# catalog-date 2009-09-03 13:00:14 +0200
# catalog-license lppl1.3
# catalog-version 1.1a
Name:		texlive-pagenote
Version:	1.1a
Release:	2
Summary:	Notes at end of document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pagenote
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagenote.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagenote.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagenote.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The pagenote package provides tagged notes on a separate page
(also known as 'end notes'). Unless the memoir class is used,
the package requires the ifmtarg package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pagenote/pagenote.sty
%doc %{_texmfdistdir}/doc/latex/pagenote/README
%doc %{_texmfdistdir}/doc/latex/pagenote/pagenote.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pagenote/pagenote.dtx
%doc %{_texmfdistdir}/source/latex/pagenote/pagenote.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-2
+ Revision: 754618
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-1
+ Revision: 719181
- texlive-pagenote
- texlive-pagenote
- texlive-pagenote
- texlive-pagenote

