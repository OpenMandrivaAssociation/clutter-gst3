%define	url_ver	%(echo %{version} | cut -d. -f1,2)
%define oname clutter-gst

%define api	3.0
%define major	0
%define gstapi	1.0
%define libname	%mklibname clutter-gst %{api} %{major}
%define devname	%mklibname -d clutter-gst %{api}
%define girname	%mklibname clutter-gst-gir %{api}
%define gstname	gstreamer%{gstapi}-gstclutter3

Summary:	GST video texture actor and audio player object for Clutter
Name:		clutter-gst3
Version:	3.0.27
Release:	2
License:	LGPLv2+
Group:		Graphics
Url:		http://clutter-project.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/clutter-gst/%{url_ver}/%{oname}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	docbook-dtd412-xml
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-base-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-video-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-audio-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-tag-%{gstapi})

%description
An integration library for using GStreamer with Clutter.
GST video texture actor and audio player object.

%package -n	%{libname}
Summary:	GST video texture actor and audio player object for Clutter
Group:		Graphics
Requires:	gstreamer%{gstapi}-plugins-base

%description -n	%{libname}
An integration library for using GStreamer with Clutter.
GST video texture actor and audio player object.

%package -n	%{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n	%{girname}
GObject Introspection interface description for %{name}.

%package -n	%{devname}
Summary:	Development headers/libraries for %{name}
Group:		Development/X11
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}

%description -n	%{devname}
Development headers/libraries for %{name}.

%package -n	%{gstname}
Summary:	Gstreamer plugin for %{name}
Group:		System/Libraries

%description -n	%{gstname}
Standalone gstreamer plugin for %{name}.

%prep
%setup -qn %{oname}-%{version}

%build
%configure \
	--enable-gtk-doc \
	--enable-introspection

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/lib%{oname}-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/ClutterGst-%{api}.typelib

%files -n %{devname}
%{_libdir}/pkgconfig/%{oname}-%{api}.pc
%{_libdir}/lib%{oname}-%{api}.so
%dir %{_includedir}/clutter-gst-%{api}/%{oname}
%{_includedir}/clutter-gst-%{api}/%{oname}/*.h
%{_datadir}/gir-1.0/ClutterGst-%{api}.gir
%dir %{_datadir}/gtk-doc/html/%{oname}-%{api}
%doc %{_datadir}/gtk-doc/html/%{oname}-%{api}/*

%files -n %{gstname}
#{_libdir}/gstreamer-%{gstapi}/libgstclutter-%{api}.so
#{_libdir}/gstreamer-1.0/libcluttergst3.so-3.0*
%{_libdir}/gstreamer-1.0/libcluttergst3.so
