%ifarch %{ocaml_native_compiler}
%global native_compiler 1
%else
%global native_compiler 0
%endif

Name:           ocaml-re
Version:        1.4.1
Release:        1%{?dist}
Summary:        A regular expression library for OCaml

License:        LGPLv2 with exceptions
URL:            https://github.com/ocaml/ocaml-re
Source0:        https://github.com/ocaml/%{name}/archive/ocaml-re-%{version}/ocaml-re-%{version}.tar.gz
# Without this, the re_pcre.ml file was installed. The problem is already fixed in master.

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc

%description 
A pure OCaml regular expression library. Supports Perl-style regular
expressions, Posix extended regular expressions, Emacs-style regular
expressions, and shell-style file globbing.  It is also possible to
build regular expressions by combining simpler regular expressions.
There is also a subset of the PCRE interface available in the Re.pcre
library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocaml-re-ocaml-re-%{version}

%build
ocaml setup.ml -configure --destdir $RPM_BUILD_ROOT
make
make doc

%install
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc CHANGES
%doc LICENSE
%doc README.md
%{_libdir}/ocaml/re
%if %{native_compiler}
%exclude %{_libdir}/ocaml/re/*.a
%exclude %{_libdir}/ocaml/re/*.cmxa
%exclude %{_libdir}/ocaml/re/*.cmx
%endif
%exclude %{_libdir}/ocaml/re/*.mli

%files devel
%doc re-api.docdir/*
%exclude /usr/local/share/doc/re/
%if %{native_compiler}
%{_libdir}/ocaml/re/*.a
%{_libdir}/ocaml/re/*.cmx
%{_libdir}/ocaml/re/*.cmxa
%endif
%{_libdir}/ocaml/re/*.mli

%changelog
* Thu Sep 3 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.4.1-1
- New upstream release
- Remove upstreamed patch

* Tue Feb 24 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.2.2-4
- Fix missing 'isa' macro in devel depends

* Sat Jan 24 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.2.2-3
- Change patch filename to have .patch suffix
- Remove whitespace

* Fri Dec 12 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.2.2-2 
- Minor updates to the SPEC file. Now rpmlint gives no errors.

* Sat Jun  7 2014 David Scott <dave.scott@citrix.com> - 1.2.2-1
- Update to 1.2.2

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 1.2.1-2
- Split files correctly between base and devel packages

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 1.2.1-1
- Initial package

