%global tl_name pagenote
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1a
Release:	%{tl_revision}.1
Summary:	Notes at end of document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pagenote
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pagenote.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pagenote.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pagenote.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The pagenote package provides tagged notes on a separate page (also
known as 'end notes'). Unless the memoir class is used, the package
requires the ifmtarg package.

