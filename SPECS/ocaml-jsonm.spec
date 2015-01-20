%ifarch %{ocaml_native_compiler}
%global native_compiler 1
%else
%global native_compiler 0
%endif

Name:           ocaml-jsonm
Version:        0.9.1
Release:        2%{?dist}
Summary:        Non-blocking streaming JSON codec for OCaml
License:        BSD
URL:            http://erratique.ch/software/jsonm
Source0:        https://github.com/dbuenzli/jsonm/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         ocaml-jsonm-setup.ml.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-uutf-devel

%description
Jsonm is a non-blocking streaming codec to decode and encode the JSON
data format. It can process JSON text without blocking on IO and
without a complete in-memory representation of the data.

The alternative "uncut" codec also processes whitespace and
(non-standard) JSON with JavaScript comments.

Jsonm is made of a single module and depends on [Uutf][1]. It is
distributed under the BSD license.

[1]: http://erratique.ch/software/uutf

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-uutf-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n jsonm-%{version}
%patch0 -p1

%build
ocaml setup.ml -configure --prefix %{_prefix} \
      --libdir %{_libdir} \
      --libexecdir %{_libexecdir} \
      --exec-prefix %{_exec_prefix} \
      --bindir %{_bindir} \
      --sbindir %{_sbindir} \
      --mandir %{_mandir} \
      --datadir %{_datadir} \
      --localstatedir %{_localstatedir} \
      --sharedstatedir %{_sharedstatedir} \
      --destdir $RPM_BUILD_ROOT
ocaml setup.ml -build 

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p %{buildroot}/%{_bindir}
ocaml setup.ml -install
rm %{buildroot}/%{_bindir}/ocamltweets

%files
%doc CHANGES
%doc README
%{_libdir}/ocaml/jsonm
%exclude %{_libdir}/ocaml/jsonm/*.mli
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/jsonm/*.a
%exclude %{_libdir}/ocaml/jsonm/*.cmxa
%exclude %{_libdir}/ocaml/jsonm/*.cmx
%endif
%{_bindir}/jsontrip

%files devel
%{_libdir}/ocaml/jsonm/*.mli
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/jsonm/*.a
%{_libdir}/ocaml/jsonm/*.cmxa
%{_libdir}/ocaml/jsonm/*.cmx
%endif

%changelog
* Mon Jan 19 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.1-2
- Minor fixes

* Thu Oct 16 2014 David Scott <dave.scott@citrix.com> - 0.9.1-1
- Initial package
