# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pagenote
# catalog-date 2009-09-03 13:00:14 +0200
# catalog-license lppl1.3
# catalog-version 1.1a
Name:		texlive-pagenote
Version:	1.1a
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The pagenote package provides tagged notes on a separate page
(also known as 'end notes'). Unless the memoir class is used,
the package requires the ifmtarg package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pagenote/pagenote.sty
%doc %{_texmfdistdir}/doc/latex/pagenote/README
%doc %{_texmfdistdir}/doc/latex/pagenote/pagenote.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pagenote/pagenote.dtx
%doc %{_texmfdistdir}/source/latex/pagenote/pagenote.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
