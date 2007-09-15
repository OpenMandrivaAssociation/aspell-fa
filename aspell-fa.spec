%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

# NOTE: the word list wrongly uses arabic kaf instead of farsi kaf,
# it is fixed trough a script in the make section (pablo)

%define src_ver 0.02-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Persian
%define languagecode fa
%define lc_ctype fa_IR

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.02.0
Release:       %mkrel 2
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
Provides:      aspell-dictionary
Provides:      aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure
#%make

# the word list wrongly uses arabic kaf instead of farsi kaf, fixing it
cat << EOF > fixkaf.sh
#!/bin/bash
cat - | \
  sed 's/ك/ک/g' 
EOF
preunzip -c %{languagecode}.cwl | sh ./fixkaf.sh | (LC_ALL=C sort) > %{languagecode}.wl
aspell  --lang=%{languagecode} create master ./%{languagecode}.rws < %{languagecode}.wl

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 Copyright README* 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright 
%{_libdir}/aspell-%{aspell_ver}/*


